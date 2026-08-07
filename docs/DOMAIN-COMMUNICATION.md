# Domain Communication

Cross-module communication is explicit. Choose the least coupled mechanism that preserves correctness.

## 1. Application contract / facade

Use for synchronous behavior when the caller needs a result now.

Example: Billing asks Identity whether a user is active through a public application interface, not through Identity's ORM model.

## 2. Domain or application event

Use when another module reacts to something that already happened and the originating transaction does not require its result.

Example: `OrderCreated` can trigger Notification and Analytics handlers.

Events are facts, use past-tense names, and must not expose infrastructure models.

## 3. Query interface / read model

Use for cross-module reads where a purpose-built projection is clearer than loading another module's aggregate.

## 4. Shared kernel

Use only for stable primitives with truly shared meaning, such as identifiers, money primitives, base domain event types, or clock abstractions. Shared kernel changes have a high blast radius.

## Decision table

| Need | Mechanism |
|---|---|
| Immediate result from another module | Application contract |
| React after a completed business fact | Event |
| Read-only cross-module information | Query interface/read model |
| Stable universal primitive | Shared kernel |

## Prohibited shortcuts

- Importing another module's repository implementation.
- Importing another module's SQLAlchemy model.
- Writing another module's tables directly.
- Using Redis/pub-sub merely to avoid defining an in-process contract.
- Creating a global `services/` directory that bypasses module ownership.
