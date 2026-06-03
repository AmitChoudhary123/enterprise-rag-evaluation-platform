# Demo

This demo simulates an enterprise policy assistant. It loads three approved policy/SOP records, retrieves the strongest evidence for a business question, returns a cited answer, and applies a release gate.

Run:

```bash
python demo/run_demo.py
```

Expected behavior:

- Retrieves the incident escalation SOP for an incident-response question
- Returns a citation such as `SOP-017:sop.pdf`
- Prints a release-gate decision that can be used in CI or governance review

Why it matters: senior AI leaders need to show that RAG systems are not just chat interfaces. They need evidence, traceability, and measurable go/no-go controls.