# ADR-0001: Modular Monolith with DDD-lite

- Status: Accepted
- Date: 2026-08-07

## Context

StarterPython must support small projects while remaining structurally stable as business capabilities grow. A flat FastAPI project becomes coupled quickly, while full enterprise DDD/CQRS introduces ceremony before it provides value.

## Decision

Use a Modular Monolith organized by business capability. Inside modules, use Domain/Application/Infrastructure/Presentation responsibilities as needed. Apply DDD patterns selectively where business invariants justify them.

FastAPI remains a delivery adapter. SQLAlchemy and Redis are infrastructure. The domain must remain independent of these frameworks.

## Consequences

### Positive

- explicit business boundaries;
- easier incremental growth;
- testable domain/application logic;
- consistent structure for humans and AI agents;
- future extraction of a module is possible without designing for microservices today.

### Trade-offs

- developers must respect module ownership;
- some cross-module use cases require explicit contracts/events;
- documentation discipline is necessary to prevent architecture drift.

## Rejected alternatives

- Flat `routers/services/models` architecture: simple initially but weak business boundaries.
- Microservices-first: operational complexity is unjustified for a starterkit baseline.
- Full CQRS/event sourcing by default: too much ceremony for general-purpose projects.
