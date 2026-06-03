from pathlib import Path
from src.rag_platform.main import answer_with_citations, load_documents, score_answer


def test_rag_demo_returns_citation_and_gate():
    docs = load_documents(Path("data/sample_documents.csv"))
    result = answer_with_citations("critical AI incident escalation", docs)
    assert result["citations"]
    assert result["release_gate"]["pass"] is True


def test_rag_gate_requires_citation():
    assert score_answer(False, 0.9, 0.9)["pass"] is False