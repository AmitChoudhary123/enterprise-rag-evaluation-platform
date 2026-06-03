from pathlib import Path
from src.rag_platform.main import answer_with_citations, load_documents

if __name__ == "__main__":
    docs = load_documents(Path("data/sample_documents.csv"))
    result = answer_with_citations("How fast should critical AI incidents be escalated?", docs)
    print("Question:", result["question"])
    print("Answer:", result["answer"])
    print("Citations:", ", ".join(result["citations"]))
    print("Release gate:", result["release_gate"])