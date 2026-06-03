from src.rag_platform.main import score_answer


def test_rag_gate_requires_citation():
    result = score_answer(has_citation=False, retrieval_score=0.95, groundedness=0.95)
    assert result["pass"] is False


def test_rag_gate_passes_grounded_answer():
    result = score_answer(has_citation=True, retrieval_score=0.86, groundedness=0.9)
    assert result["pass"] is True