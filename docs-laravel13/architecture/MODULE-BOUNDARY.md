# Module Boundary

## Definisi

Module Boundary adalah batas capability tingkat atas yang mengelompokkan beberapa module yang memiliki konteks bisnis, vocabulary, ownership, dan dependency yang berdekatan.

Struktur resmi:

```text
app/Module/{ModuleBoundary}/{Module}
```

Contoh:

```text
app/Module/AccessControl/
├── Role/
├── Permission/
├── Policy/
└── UserAccess/
```

`AccessControl` adalah boundary. `Role` dan `Permission` adalah module.

## Boundary Bukan Folder Organisasi Biasa

Boundary harus memiliki:

- tujuan bisnis yang jelas;
- vocabulary sendiri;
- daftar module yang dimiliki;
- ownership data;
- public contract untuk boundary lain;
- published/consumed event;
- aturan dependency;
- keputusan arsitektur yang relevan.

## Dokumentasi Boundary

Setiap boundary wajib memiliki dokumentasi, minimal melalui `BOUNDARY-SPEC.md` atau README boundary.

Contoh:

```text
app/Module/AccessControl/README.md
```

Dokumen boundary menjelaskan capability keseluruhan dan tidak menggantikan README masing-masing module.

## Evolusi Boundary

Boundary boleh bertambah module secara incremental tanpa mengubah arsitektur project.

```text
Awal:
AccessControl
├── Role
└── Permission

Berkembang:
AccessControl
├── Role
├── Permission
├── Policy
├── Scope
└── Delegation
```

Penambahan module baru mengikuti alur:

```text
Update Boundary Spec
    -> Module Spec
    -> Feature Spec
    -> Implementation Plan
    -> Implementasi
    -> Change Record
```

## Aturan Lintas Boundary

Boundary lain tidak boleh bergantung pada internal module secara sembarang. Komunikasi lintas boundary harus melewati public application contract, query interface/read model, atau event yang dipublikasikan oleh owning boundary.