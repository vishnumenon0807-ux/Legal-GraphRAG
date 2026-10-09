"""Parse a statute that exists only as PDF (the Rules, SEBI regulations).

STAGE 1b - not written yet. Needed only if the corpus widens beyond the
Companies Act, which is the open decision.

The Akoma Ntoso parser gets hierarchy for free. A PDF does not, so this module
has to reconstruct it: detect section headings, attach subsection and clause
numbering, drop running headers/footers and amendment footnotes, and emit the
same node shape as parse.akoma so everything downstream is unchanged.

Emit: [{id, type, section, num, parent, depth, heading, text, full_text}]
with ids prefixed by the corpus key from config.CORPORA.
"""
