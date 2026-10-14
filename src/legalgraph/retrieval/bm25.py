"""Lexical baseline. STAGE 3.

BM25 over section full text. This is the baseline the graph has to beat, so it
gets a fair effort: legal-specific stopwords, light suffix normalisation, and
k1/b exposed for tuning rather than left at library defaults.

Deliberately not stemmed with a real stemmer. Statutory text is formulaic and
aggressive stemming merges distinct terms of art ("security"/"securities" is
fine to merge, "deposit"/"deposition" is not). The crude plural rule below is
what helped on inspection; anything more needs measuring first.
"""

import re

from rank_bm25 import BM25Okapi

# Words that appear in nearly every section of an Act and carry no signal.
# Leaving these in makes every query match every section a little.
LEGAL_STOPWORDS = {
    "the", "a", "an", "of", "in", "to", "for", "or", "and", "by", "be", "is",
    "are", "was", "were", "shall", "may", "any", "such", "this", "that", "with",
    "as", "under", "not", "no", "on", "at", "from", "it", "its", "which", "who",
    "whom", "been", "has", "have", "had", "if", "then", "than", "so", "but",
    "all", "each", "other", "there", "where", "when", "while", "being", "do",
    "does", "section", "sub", "subsection", "clause", "provided", "provisions",
    "provision", "act", "company", "companies", "case", "manner", "respect",
    "purposes", "purpose", "accordance", "thereof", "therein", "hereby",
    "aforesaid", "said", "same", "specified", "prescribed", "referred",
}


def normalise(token: str) -> str:
    """Crude plural/possessive stripping. Conservative on purpose."""
    if len(token) > 4:
        if token.endswith("ies"):
            return token[:-3] + "y"
        if token.endswith("ses") or token.endswith("xes"):
            return token[:-2]
        if token.endswith("s") and not token.endswith("ss"):
            return token[:-1]
    return token


def tokenise(text: str) -> list[str]:
    raw = re.findall(r"[a-z]+", text.lower())
    return [normalise(t) for t in raw if len(t) > 2 and t not in LEGAL_STOPWORDS]


class BM25Retriever:
    def __init__(self, units: list[dict], k1: float = 1.5, b: float = 0.75):
        self.units = units
        self.ids = [u["id"] for u in units]
        corpus = [tokenise(u["text"]) for u in units]
        self.model = BM25Okapi(corpus, k1=k1, b=b)

    def search(self, query: str, k: int = 10) -> list[str]:
        scores = self.model.get_scores(tokenise(query))
        ranked = sorted(range(len(scores)), key=lambda i: -scores[i])
        return [self.ids[i] for i in ranked[:k]]

    def search_scored(self, query: str, k: int = 10) -> list[tuple[str, float]]:
        scores = self.model.get_scores(tokenise(query))
        ranked = sorted(range(len(scores)), key=lambda i: -scores[i])
        return [(self.ids[i], float(scores[i])) for i in ranked[:k]]
