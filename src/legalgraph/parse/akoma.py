"""Parse an Akoma Ntoso statute XML into addressable clause nodes.

Usage: python3 -I src/parse_act.py <act.xml> <out.json>

Produces a flat list of clause nodes. Every node has a canonical citation-style
id so that a reference found in the text ("clause (a) of sub-section (1) of
section 2") can be resolved to exactly one node.

Granularity: section > subsection > item/paragraph. Section-level headings are
kept because references in Indian statutes often cite a section as a whole.
"""

import json
import re
import sys
import xml.etree.ElementTree as ET

NS = {"an": "http://www.akomantoso.org/2.0"}


def clean(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


NUMBERED = ("subsection", "paragraph", "item")
SKIP = ("num", "heading", "subheading")


def node_text(el, include_children=False):
    """Text of this element in document order.

    include_children=False gives the node's OWN text: the list introduction and
    any proviso paragraphs, but not the text of deeper numbered units, which are
    separate nodes. include_children=True gives the whole subtree, which is what
    you want when retrieving a section as a single unit.
    """
    parts = []

    def walk(e):
        for child in e:
            tag = child.tag.split("}")[-1]
            if tag in SKIP:
                continue
            if tag in NUMBERED:
                if not include_children:
                    continue
                num_el = child.find("an:num", NS)
                if num_el is not None and num_el.text:
                    parts.append(clean(num_el.text))
                walk(child)
                continue
            if tag in ("p", "listIntroduction"):
                parts.append("".join(child.itertext()))
            else:
                walk(child)

    walk(el)
    return clean(" ".join(parts))


def strip_num(raw):
    """'6.' -> '6' ; '(1)' -> '1' ; '(a)' -> 'a'"""
    return clean(raw).strip(".()" ).strip()


def parse(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    body = root.find(".//an:body", NS)
    if body is None:
        raise SystemExit("no <body> found")

    nodes = []

    def walk_children(parent_el, sec_num, prefix, parent_id, depth):
        """Recurse through subsection / paragraph / item under a section."""
        for child in parent_el:
            tag = child.tag.split("}")[-1]
            if tag not in ("subsection", "paragraph", "item"):
                # descend through wrappers that can contain numbered units
                if tag in ("content", "blockList"):
                    walk_children(child, sec_num, prefix, parent_id, depth)
                continue
            num_el = child.find("an:num", NS)
            num = strip_num(num_el.text if num_el is not None else "")
            if not num:
                continue
            cid = f"{prefix}({num})"
            nodes.append({
                "id": cid,
                "type": tag,
                "section": sec_num,
                "num": num,
                "parent": parent_id,
                "depth": depth,
                "heading": "",
                "text": node_text(child),
                "full_text": node_text(child, include_children=True),
            })
            walk_children(child, sec_num, cid, cid, depth + 1)

    for chapter in body.iter():
        if chapter.tag.split("}")[-1] != "section":
            continue
        sec = chapter
        num_el = sec.find("an:num", NS)
        head_el = sec.find("an:heading", NS)
        sec_num = strip_num(num_el.text if num_el is not None else "")
        if not sec_num:
            continue
        sid = f"s{sec_num}"
        nodes.append({
            "id": sid,
            "type": "section",
            "section": sec_num,
            "num": sec_num,
            "parent": None,
            "depth": 0,
            "heading": clean("".join(head_el.itertext()) if head_el is not None else "").rstrip("—-– "),
            "text": node_text(sec),
            "full_text": node_text(sec, include_children=True),
        })
        walk_children(sec, sec_num, sid, sid, 1)

    return nodes


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    nodes = parse(sys.argv[1])
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(nodes, f, ensure_ascii=False, indent=1)

    by_type = {}
    for n in nodes:
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1
    empty = sum(1 for n in nodes if not n["text"])
    chars = sum(len(n["text"]) for n in nodes)
    print(f"nodes: {len(nodes)}")
    for t, c in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t:<12} {c}")
    print(f"empty-text nodes: {empty}  ({100*empty/len(nodes):.1f}%)")
    print(f"total text: {chars:,} chars")
    print("sample ids:", ", ".join(n["id"] for n in nodes[:8]))


if __name__ == "__main__":
    main()
