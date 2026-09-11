# Contributing to 3D Visualization Hub

## Authority and evidence boundary

This repository is an **experimental visualization workstream**. Current authority comes from repository-local source, CI evidence, dated deployment/runtime evidence where available, and explicit maintainer decisions.

Historical references to DGAF, PDMAL, Agent Amethyst, COLLEEN, or GCP phase labels describe project lineage or intended integration context. They do not confer autonomous governance, certification, production status, or cross-repository validation.

## What this repository does

- Interactive 3D and multidimensional visualization via Plotly, Matplotlib, and Streamlit where implemented.
- Experimental phi-harmonic, modal, topology, and modeled-state visualization.
- Cloud deployment/storage integration where actually configured in source.
- Rendering and inspection of external or ecosystem-derived data where an implemented data path exists.

A visualization does not prove the modeled phenomenon. A cloud configuration does not prove a live service. A repository-local cost target does not prove external billing enforcement.

## Contribution rules

1. Open an issue with a clear visualization or infrastructure use case.
2. Branch from current `main`.
3. Keep implementation claims tied to source/tests that exist in this repository.
4. For GCP or deployment changes, distinguish **configured target** from **observed live runtime**.
5. If making a live deployment claim, include dated source → deployment → runtime evidence.
6. If making a cost-control claim, identify the actual external enforcement mechanism and dated billing/telemetry evidence; otherwise describe it as a target or configuration only.
7. Submit screenshots when they help review rendered output, but treat screenshots as rendering evidence only—not mathematical, scientific, or production validation.
8. Do not infer DGAF/PDMAL state from references or shared terminology.

## Technical references

The repository may contain or target:

- Google Cloud Run configuration;
- GCP storage configuration;
- OpenTelemetry instrumentation;
- Plotly, Matplotlib, and Streamlit rendering;
- phi-harmonic or PDMAL-related visualization vocabulary.

Verify the current source before treating any of these as implemented or active.

## IP notice

Project-specific constants, tuning tables, and optimization details may be intentionally omitted from public artifacts. Contribution review must not treat missing proprietary detail as evidence for or against broader scientific claims.

## Related repositories

- [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) — separate governance/evaluation research track
- [Acoustic-mesh](https://github.com/ndrorchestration/Acoustic-mesh) — separate acoustic/signal-processing track
- [Driftwatch](https://github.com/ndrorchestration/Driftwatch) — separate drift-detection track
- [ai-governance-frameworks](https://github.com/ndrorchestration/ai-governance-frameworks) — separate standards-alignment track

Cross-repository references do not transfer validation.
