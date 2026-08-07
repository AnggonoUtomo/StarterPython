# ADR-0001: Modular Monolith dengan DDD-lite

- Status: Diterima
- Tanggal: 2026-08-07

## Konteks

StarterPython harus dapat digunakan untuk project kecil namun tetap memiliki struktur yang stabil ketika kapabilitas bisnis bertambah. Project FastAPI yang flat akan cepat mengalami coupling, sedangkan DDD/CQRS enterprise penuh menambahkan terlalu banyak ceremony sebelum memberikan manfaat nyata.

## Keputusan

Gunakan Modular Monolith yang diorganisasi berdasarkan kapabilitas bisnis. Di dalam modul, gunakan tanggung jawab Domain/Application/Infrastructure/Presentation sesuai kebutuhan. Terapkan pola DDD secara selektif ketika business invariant memang membutuhkannya.

FastAPI tetap menjadi delivery adapter. SQLAlchemy dan Redis berada pada infrastructure. Domain harus independen dari framework tersebut.

## Konsekuensi

### Positif

- boundary bisnis menjadi eksplisit;
- pertumbuhan incremental lebih mudah;
- logic domain/application lebih mudah diuji;
- struktur konsisten untuk developer manusia maupun AI agent;
- ekstraksi modul pada masa mendatang tetap memungkinkan tanpa harus mendesain microservices sejak awal.

### Trade-off

- developer harus disiplin menghormati ownership modul;
- beberapa use case lintas modul membutuhkan contract/event yang eksplisit;
- disiplin dokumentasi diperlukan untuk mencegah architecture drift.

## Alternatif yang Ditolak

- Arsitektur flat `routers/services/models`: sederhana pada awalnya tetapi memiliki boundary bisnis yang lemah.
- Microservices-first: kompleksitas operasional tidak sebanding untuk baseline starterkit.
- Full CQRS/event sourcing secara default: terlalu banyak ceremony untuk project general-purpose.

## Kebijakan Bahasa

ADR ini dan seluruh ADR berikutnya wajib ditulis dalam Bahasa Indonesia. Istilah teknis Bahasa Inggris boleh dipertahankan jika lebih presisi, tetapi keputusan, alasan, konsekuensi, dan konteks harus dijelaskan dalam Bahasa Indonesia.
