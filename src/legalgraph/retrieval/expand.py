"""Graph expansion on top of a base retriever. STAGE 4.

Take the base retriever's top-k clauses, walk outgoing reference edges, add the
targets. The ablation is the experiment: expansion off vs on, and depth 1 vs 2
vs 3, measured against the gold clause sets.

Expect over-expansion to hurt precision at some depth. Report that curve; it is
the finding most papers in this area leave out.
"""
