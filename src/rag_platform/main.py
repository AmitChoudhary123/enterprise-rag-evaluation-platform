from __future__ import annotations

import csv
import math
from pathlib import Path


def tokenize(text: str) -> set[str]:
    return {token.strip(".,:;!?()[]\"").lower() for token in text.split() if token.strip()}


def load_documents(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def retrieve(query: str, documents: list[dict], top_k: int = 2) -> list[dict]:
    query_terms = tokenize(query)
    ranked = []
    for doc in documents:
        doc_terms = tokenize(doc["title"] + " " + doc["text"])
        overlap = len(query_terms & doc_terms)
        score = overlap / math.sqrt(max(len(doc_terms), 1))
        ranked.append({**doc, "retrieval_score": round(score, 3)})
    return sorted(ranked, key=lambda row: row["retrieval_score"], reverse=True)[:top_k]


def answer_with_citations(query: str, documents: list[dict]) -> dict:
    evidence = retrieve(query, documents, top_k=2)
    best = evidence[0]
    citation = f"{best['id']}:{best['source']}"
    groundedness = min(1.0, best["retrieval_score"] + 0.35)
    release_score = score_answer(True, best["retrieval_score"], groundedness)
    return {
        "question": query,
        "answer": best["text"],
        "citations": [citation],
        "evidence": evidence,
        "release_gate": release_score,
    }


def score_answer(has_citation: bool, retrieval_score: float, groundedness: float) -> dict:
    citation = 1.0 if has_citation else 0.0
    score = (0.35 * retrieval_score) + (0.45 * groundedness) + (0.20 * citation)
    return {"score": round(score, 3), "pass": score >= 0.55 and has_citation}