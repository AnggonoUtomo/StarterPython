# Module Guide

A module represents a business capability with an explicit boundary, vocabulary, and ownership of its persistence model.

## When to create a module

Create one when the capability has meaningful business rules, its own lifecycle/data ownership, or needs an independent boundary. Do not create modules for generic helpers.

## Minimal module

```text
modules/billing/
├── application/
│   └── create_invoice.py
├── domain/
│   └── invoice.py
├── infrastructure/
│   └── invoice_repository.py
└── presentation/
    ├── routes.py
    └── schemas.py
```

A module may start smaller. Add folders because a responsibility exists, not because a template says every folder must exist.

## Feature implementation sequence

1. Write the feature/module spec when behavior is non-trivial.
2. Identify invariants and ownership.
3. Define domain concepts.
4. Define required application input/output.
5. Define contracts for persistence/external dependencies.
6. Implement infrastructure adapters.
7. Expose through presentation.
8. Add unit/integration/feature tests.
9. Update docs/ADR when architecture changed.

## Naming

Use business language: `CreateInvoice`, `Membership`, `TradingSignal`. Avoid weak names such as `Manager`, `Helper`, `CommonService`, or `Utils` when a more precise capability exists.

## Boundary rule

This is forbidden:

```python
from starterpython.modules.users.infrastructure.models import UserModel
```

from another module.

Prefer a stable application-facing contract such as `UserReader`, `UserAccess`, or an event published by the owning module.
