# Enterprise RAG Evaluation Platform

A production-oriented RAG blueprint for governed, measurable, enterprise knowledge retrieval.

## Business problem

Enterprises are moving documents, policies, service knowledge, and operating procedures into GenAI workflows, but many RAG systems fail because they cannot prove accuracy, cite sources, or detect regressions.

## Why it matters

Enterprise AI portfolios are judged by business outcomes, architecture quality, reliability, governance, and reproducibility. This repository is designed to demonstrate practical delivery thinking rather than a tutorial-only implementation.

## Solution overview

This repository defines a domain-specific Ask My Docs platform with hybrid retrieval, reranking, citation enforcement, answer-quality scoring, and release gates for retrieval and generation quality.

## Architecture

The solution is organized into business context, architecture documentation, source contracts, tests, and CI validation. See docs/architecture.md for the reference design and operating model.

## Tech stack

Python, FastAPI, BM25, vector search, reranking, RAG evaluation, pytest, GitHub Actions

## Repository structure

`	ext
.
|-- .github/workflows/ci.yml
|-- docs/
|   |-- architecture.md
|   |-- business-case.md
|   -- roadmap.md
|-- src/
|   -- rag_platform/
|       |-- __init__.py
|       -- main.py
|-- tests/
|   -- test_contract.py
|-- .gitignore
|-- LICENSE
|-- README.md
-- requirements.txt
`

## Quick start

`ash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
pytest -q
`

## Roadmap

- Add richer domain examples and sample datasets
- Expand implementation into a deployable FastAPI service
- Add dashboards and architecture diagrams
- Add evaluation reports with measurable baseline and target metrics
- Package templates for executive review and delivery governance

## Enterprise relevance

This repository shows how I approach AI delivery as a senior enterprise leader: start from the business problem, design the operating model, define measurable controls, and make the implementation reproducible enough for teams to extend.