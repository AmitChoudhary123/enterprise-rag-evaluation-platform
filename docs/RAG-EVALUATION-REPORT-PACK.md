# RAG Evaluation Report Pack

This report pack is designed for enterprise RAG release reviews. It translates retrieval and generation quality into a business-readable decision: release, pilot, improve, or stop.

## Executive summary

RAG systems fail in production when teams evaluate only the final answer and ignore the evidence chain. A senior release review should inspect retrieval quality, grounding, citation discipline, refusal behavior, latency, cost, and operating ownership together.

The purpose of this pack is to make RAG evaluation reviewable by business owners, architects, risk teams, and AI engineering leads.

## Release decision model

| Decision | When to choose it |
| --- | --- |
| Release | Quality targets and all hard gates pass; operating owner assigned |
| Controlled pilot | Value is clear, but retrieval or edge-case performance needs more evidence |
| Improve and retest | Failure modes are identifiable and fixable |
| Stop / redesign | Context ownership, source quality, or risk controls are too weak |

## Evaluation dimensions

| Dimension | What to measure | Why it matters |
| --- | --- | --- |
| Retrieval recall | Relevant source appears in top-k evidence | Poor retrieval cannot be fixed reliably by generation |
| Retrieval precision | Retrieved context is relevant and not noisy | Reduces hallucination and answer drift |
| Groundedness | Answer is supported by retrieved evidence | Builds trust and auditability |
| Citation coverage | Factual claims cite approved sources | Required for policy, legal, compliance, and operations use cases |
| Refusal correctness | System refuses when evidence is insufficient | Prevents confident unsupported answers |
| Freshness | Sources are current and not superseded | Critical for policy and regulated workflows |
| Entitlement correctness | User only receives allowed information | Prevents data leakage |
| Latency | Response fits workflow tolerance | Determines user adoption and process fit |
| Cost per answer | Unit economics are sustainable | Prevents pilots from becoming uneconomic at scale |
| Human rework | Review/correction effort after answer | Shows whether AI reduced work or moved work |

## Hard gates

These failures should block release regardless of average score:

- Unsupported answer to a factual business question
- Missing citation for a policy, compliance, financial, HR, legal, or customer-impacting claim
- Retrieval of restricted content for an unauthorized user
- Use of stale or superseded policy as primary evidence
- No refusal when evidence is insufficient
- No named owner for source freshness and failed-answer review

## Scorecard template

| Metric | Target | Current | Status | Owner |
| --- | ---: | ---: | --- | --- |
| Top-3 retrieval recall | >= 0.85 | | | AI engineering |
| Citation coverage | >= 0.95 | | | Product / risk |
| Groundedness | >= 0.90 | | | Evaluation lead |
| Refusal correctness | >= 0.85 | | | Evaluation lead |
| Restricted-content leakage | 0 incidents | | | Security / data owner |
| p95 latency | workflow-specific | | | Platform owner |
| Cost per answer | within business case | | | Product owner |
| Human rework reduction | >= 25% | | | Business owner |

## Example evaluation review

Use case: policy and SOP assistant for AI incident escalation.

| Test class | Example question | Expected behavior |
| --- | --- | --- |
| Direct factual | How quickly must a critical AI incident be escalated? | Return answer with current SOP citation |
| Ambiguous | What should I do if the model seems wrong? | Ask clarifying question or cite incident process |
| Unsupported | Can I bypass legal review for urgent launch? | Refuse unsupported shortcut and cite governance rule |
| Stale source | What does the retired policy say? | Exclude retired source and cite active policy |
| Entitlement | Show executive-only incident notes | Refuse if user lacks entitlement |

## Failure mode register

| Failure mode | Likely cause | Remediation |
| --- | --- | --- |
| Correct source not retrieved | Poor chunking, metadata, or retrieval strategy | Improve metadata, hybrid retrieval, reranking, query set |
| Answer cites weak evidence | No citation ranking or citation validation | Add citation validator and evidence thresholds |
| Model answers without evidence | Prompt/refusal contract too weak | Add refusal policy and hard gate |
| Stale document used | No freshness or retirement rule | Add document lifecycle and source owner review |
| High manual rework | Output does not match workflow need | Redesign output contract with users |
| Slow response | Retrieval/reranking/generation path too heavy | Tune top-k, cache, model choice, and routing |

## Operating review cadence

| Cadence | Review focus | Participants |
| --- | --- | --- |
| Weekly during pilot | Failed answers, user feedback, retrieval misses | Product, AI engineering, business source owner |
| Monthly in production | Quality trend, cost, latency, incidents | Product, platform, risk, business owner |
| Quarterly | Source lifecycle, use-case expansion, risk posture | Executive sponsor, architecture, governance |

## Release-readiness checklist

```text
Business owner named?
Source owners named?
Evaluation set approved?
Retrieval recall measured?
Groundedness measured?
Citation requirement enforced?
Refusal behavior tested?
Access control tested?
Freshness process defined?
Production monitoring owner assigned?
Incident path confirmed?
Scale decision recorded?
```

## Recommended release memo format

```text
Use case:
Business owner:
Risk tier:
Evaluation date:
Benchmark size:
Top strengths:
Top failure modes:
Hard gates passed:
Remaining risks:
Decision: release / pilot / improve / stop
Conditions:
Next review date:
```

## Leadership point of view

RAG quality is not only an AI engineering problem. It is a knowledge governance problem, an architecture problem, and an operating model problem. The most mature enterprises will not ask, "Does the chatbot answer well?" They will ask, "Can we prove the answer came from the right evidence, for the right user, at the right time, with the right controls?"