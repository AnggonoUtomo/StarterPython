# Dokumentasi Laravel 13 — Modular Monolith DDD-lite

Direktori ini berisi dokumentasi arsitektur dan operating system pengembangan khusus Laravel 13. Dokumentasi ini sengaja dipisahkan dari dokumentasi StarterPython agar tidak tercampur.

## Kebijakan Bahasa

Semua dokumentasi di dalam `docs-laravel13/` wajib menggunakan Bahasa Indonesia. Nama class, method, variable, namespace, route, command, event, dan identifier source code tetap menggunakan Bahasa Inggris mengikuti konvensi Laravel/PHP, kecuali istilah domain lebih tepat dipertahankan dalam bahasa aslinya.

## Struktur Arsitektur Utama

Struktur modul menggunakan pola:

```text
app/Module/{ModuleBoundary}/{Module}
```

Contoh:

```text
app/
└── Module/
    └── AccessControl/
        ├── Role/
        ├── Permission/
        ├── Policy/
        └── UserAccess/
```

`AccessControl` adalah **Module Boundary**, sedangkan `Role`, `Permission`, `Policy`, dan `UserAccess` adalah **Module** di dalam boundary tersebut.

## Urutan Bacaan

1. `architecture/ARCHITECTURE.md`
2. `architecture/MODULE-BOUNDARY.md`
3. `architecture/MODULE-ARCHITECTURE.md`
4. `architecture/DOMAIN-COMMUNICATION.md`
5. `architecture/CROSS-BOUNDARY-COMMUNICATION.md`
6. `development/PERSISTENCE-CONVENTIONS.md`
7. `development/EVENT-QUEUE-GUIDE.md`
8. `development/TESTING-GUIDE.md`
9. `ai/AI-DEVELOPMENT-GUIDE.md`
10. template pada `templates/`

## Empat Level Documentation OS

```text
LEVEL 1 — PROJECT GOVERNANCE
README
ARCHITECTURE
AI DEVELOPMENT GUIDE
DEFINITION OF DONE

LEVEL 2 — ARCHITECTURE
MODULE BOUNDARY
MODULE ARCHITECTURE
DOMAIN COMMUNICATION
CROSS-BOUNDARY COMMUNICATION
PERSISTENCE
EVENT / QUEUE
TESTING

LEVEL 3 — BOUNDARY & MODULE KNOWLEDGE
BOUNDARY-SPEC
MODULE-SPEC
MODULE README

LEVEL 4 — INCREMENTAL WORK RECORD
FEATURE-SPEC
IMPLEMENTATION-PLAN
CHANGE-RECORD
BUG-INVESTIGATION
ADR
```

Dokumentasi ini menjadi baseline kerja manusia maupun AI/Codex untuk project Laravel 13 yang menggunakan Modular Monolith + DDD-lite.