# backend-playbook

A public, implementation-first backend engineering journey.

This repository is organized as a long-term roadmap where each topic is learned by building small, runnable systems instead of passively consuming tutorials.

## Current Scope
Phase 1 only.

- Language core (Python-first, runtime-level understanding)
- Internet foundations (DNS, TCP, HTTP request-response internals)
- Raw HTTP server (no framework)
- Linux and CLI fluency
- SQL fundamentals
- Git beyond the basics

## Philosophy
- Learn by implementation
- Keep each exercise small and focused
- Prefer observable behavior over theory-only notes
- Build artifacts you can rerun from any machine

## Repository Structure
- phase-1-foundation: complete Phase 1 roadmap and practice areas
- phase-1-foundation/01-language-core/python-data-model-lab: active Python data model lab with exercises and tests

## Phase 1 Start Here
1. Read: phase-1-foundation/README.md
2. Begin coding: phase-1-foundation/01-language-core/python-data-model-lab
3. Implement each exercise in order
4. Add tests as behavior becomes stable

## Running The Data Model Lab
From phase-1-foundation/01-language-core/python-data-model-lab:

```bash
python run_all.py
```

To run tests (when pytest is available):

```bash
pytest tests
```

## Public Learning Intent
This repository is intentionally public so other developers can follow the same path, inspect implementations, and reuse the structure for their own backend journey.

## Planned Expansion
Additional phases and projects will be added gradually as the journey progresses.
