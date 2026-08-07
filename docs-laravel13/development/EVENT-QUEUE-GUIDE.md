# Panduan Event dan Queue Laravel 13

## Tujuan

Dokumen ini membedakan Domain Event, Application Event, Laravel Event, Listener, Queued Listener, Job, dan Notification agar tidak tercampur.

## Definisi

### Domain Event
Fakta penting yang terjadi di domain, misalnya `InvoicePaid` atau `StudentRegistered`.

### Application Event
Notifikasi pada level application boundary ketika use case selesai atau menghasilkan fakta yang relevan bagi bagian lain.

### Laravel Event
Mekanisme dispatcher/framework untuk mendistribusikan event.

### Listener
Reaction terhadap event.

### Queued Listener
Listener yang boleh dijalankan asynchronous karena transaksi asal tidak membutuhkan hasilnya segera.

### Job
Pekerjaan yang harus dieksekusi. Job bukan fakta bisnis.

### Notification
Representasi notifikasi ke channel seperti mail/database/broadcast.

## Pola

```text
PaymentConfirmed
    -> application/domain processing
    -> InvoicePaid
        -> SendReceiptListener (queue)
        -> UpdateReportListener (queue)
```

## Kapan Event Digunakan

Gunakan event ketika sesuatu **sudah terjadi** dan satu atau lebih consumer dapat bereaksi tanpa mengendalikan transaksi asal.

Jangan gunakan event sebagai pengganti function call synchronous hanya untuk terlihat decoupled.

## Transaction Safety

Event/queued listener yang bergantung pada data hasil transaksi harus dipastikan berjalan setelah transaksi berhasil commit. Jangan membiarkan consumer membaca state yang belum committed.

## Job

Gunakan Job untuk pekerjaan seperti:

- generate laporan besar;
- kirim file;
- sinkronisasi external service;
- proses batch;
- pekerjaan retryable yang tidak harus menyelesaikan HTTP request.

## Idempotency

Job dan listener yang dapat di-retry harus dirancang idempotent jika side effect dapat terulang.

## Larangan

- mengirim Eloquent model lintas boundary sebagai contract event publik;
- event bernama command seperti `CreateInvoiceEvent` padahal belum terjadi;
- menjadikan queue sebagai cara menyembunyikan coupling yang tidak terdefinisi;
- melakukan critical synchronous validation melalui queued listener;
- menaruh orkestrasi bisnis besar di listener tanpa ownership yang jelas.