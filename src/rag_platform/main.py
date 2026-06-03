def score_answer(has_citation: bool, retrieval_score: float, groundedness: float) -> dict:
    """Return a simple release-gate score for a RAG answer."""
    citation = 1.0 if has_citation else 0.0
    score = (0.35 * retrieval_score) + (0.45 * groundedness) + (0.20 * citation)
    return {"score": round(score, 3), "pass": score >= 0.75 and has_citation}