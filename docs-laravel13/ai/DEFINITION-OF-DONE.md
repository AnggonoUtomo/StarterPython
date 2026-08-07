# Definition of Done Laravel 13

Sebuah perubahan dianggap selesai ketika seluruh kondisi relevan berikut terpenuhi.

## Behavior

- requirement yang disepakati sudah terpenuhi;
- acceptance criteria dapat diverifikasi;
- error path penting sudah ditangani.

## Arsitektur

- boundary `app/Module/{ModuleBoundary}/{Module}` tetap terjaga;
- tidak ada dependency leak lintas module/boundary;
- public contract/event terdokumentasi jika berubah;
- ADR dibuat bila ada keputusan arsitektur durable.

## Persistence

- migration tersedia untuk perubahan schema;
- ownership tabel/data jelas;
- transaction boundary berada pada use case/application layer;
- tidak ada direct write ke tabel module lain tanpa contract yang sah.

## Testing

- unit/feature/integration test ditambahkan sesuai kebutuhan;
- regression test ditambahkan untuk bug yang relevan;
- seluruh test existing yang terkait tetap lolos.

## Quality

- formatter/linter/static analysis project lolos;
- tidak ada dead/debug code yang tertinggal;
- security dan authorization diperiksa jika relevan.

## Dokumentasi

- Feature Spec/Implementation Plan/Change Record tersinkronisasi;
- README boundary/module diperbarui bila contract atau responsibility berubah;
- semua dokumentasi baru/perubahan menggunakan Bahasa Indonesia.

## Operasional

- dampak queue/cache/config/env/migration/deployment dicatat bila ada;
- backward compatibility dan rollout diperiksa jika relevan.