# Panduan Pengembangan Laravel 13 dengan AI

Dokumen ini adalah kontrak kerja untuk AI/Codex pada project Laravel 13 yang menggunakan baseline ini.

## Urutan Bacaan Wajib

Sebelum perubahan non-trivial:

1. `docs-laravel13/README.md`
2. `architecture/ARCHITECTURE.md`
3. `architecture/MODULE-BOUNDARY.md`
4. `architecture/MODULE-ARCHITECTURE.md`
5. `architecture/DOMAIN-COMMUNICATION.md`
6. `architecture/CROSS-BOUNDARY-COMMUNICATION.md`
7. dokumen boundary/module terkait;
8. Feature Spec dan Implementation Plan terkait;
9. ADR relevan.

## Aturan AI

1. Pertahankan struktur `app/Module/{ModuleBoundary}/{Module}`.
2. Jangan membuat arsitektur project-wide baru untuk satu fitur.
3. Jangan melewati module ownership melalui folder global `Services`, `Helpers`, `Utils`, atau `Repositories`.
4. Jangan mengimpor Infrastructure internal lintas module/boundary.
5. Jangan menaruh business logic pada Controller, FormRequest, Service Provider, Listener, Job, atau Eloquent Model tanpa alasan arsitektur yang jelas.
6. Gunakan pola existing sebelum membuat abstraction baru.
7. Hindari abstraction spekulatif.
8. Setiap behavior baru/perubahan harus memiliki test yang sesuai.
9. Perbarui dokumentasi jika implementation mengubah kontrak, boundary, persistence, event, atau behavior penting.
10. Perubahan arsitektur durable wajib menggunakan ADR.
11. Semua dokumentasi wajib menggunakan Bahasa Indonesia.
12. Identifier source code tetap menggunakan Bahasa Inggris sesuai konvensi Laravel/PHP.
13. Jika requirement baru ditemukan saat implementasi, update spec/plan; jangan mengubah scope diam-diam.

## Workflow

```text
Context
 -> Boundary/Module Spec
 -> Feature Spec
 -> Implementation Plan
 -> Implementasi Incremental
 -> Test
 -> Change Record
 -> Sinkronisasi Dokumentasi
 -> Done
```

## Prinsip Incremental

Pekerjaan besar dipecah menjadi perubahan kecil yang dapat diverifikasi. Change Record mencatat keputusan/discovery penting, bukan setiap edit trivial.