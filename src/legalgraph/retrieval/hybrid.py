"""BM25 + dense fused with reciprocal rank fusion, then a cross-encoder
reranker. STAGE 3.

This is the real baseline. If the graph only beats plain dense retrieval, the
result is not interesting, because hybrid+rerank beats plain dense on almost
every corpus without any graph at all.
"""
