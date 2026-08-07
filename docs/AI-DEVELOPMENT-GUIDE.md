# AI Development Guide

This file is a contract for AI-assisted development in StarterPython.

## Required reading order

Before implementing a non-trivial change, read:

1. `README.md`
2. `docs/ARCHITECTURE.md`
3. `docs/MODULE-GUIDE.md`
4. `docs/DOMAIN-COMMUNICATION.md`
5. Relevant module docs/specs and ADRs.

## AI rules

1. Preserve Modular Monolith / DDD-lite boundaries.
2. Do not invent a new project-wide architecture for a feature.
3. Do not place business behavior in `core/`, `utils/`, HTTP routes, or ORM models by convenience.
4. Do not import infrastructure internals across modules.
5. Prefer an existing pattern before introducing a new abstraction.
6. Avoid speculative abstractions. Implement the smallest coherent design that supports current requirements.
7. Every behavior change needs tests at the cheapest useful level.
8. Run Ruff, Pyright, and pytest before declaring implementation complete.
9. If architecture or a durable convention changes, add/update an ADR.
10. If requirements are discovered during implementation, update the relevant spec/plan rather than silently changing scope.

## Incremental work record

For substantial work, use `docs/templates/FEATURE-SPEC.md` before implementation and `docs/templates/CHANGE-RECORD.md` during/after implementation. This keeps AI decisions reviewable and prevents undocumented architecture drift.

## Definition of done

A change is complete when behavior works, tests cover meaningful cases, static checks pass, boundaries remain valid, migration/operational effects are documented, and relevant docs are synchronized.
