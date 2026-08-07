# Panduan Pengembangan dengan AI

File ini merupakan kontrak kerja untuk pengembangan StarterPython yang dibantu AI/Codex.

## Urutan Bacaan Wajib

Sebelum mengimplementasikan perubahan yang tidak trivial, baca:

1. `README.md`
2. `docs/ARCHITECTURE.md`
3. `docs/MODULE-GUIDE.md`
4. `docs/DOMAIN-COMMUNICATION.md`
5. `docs/PERSISTENCE-CONVENTIONS.md` jika perubahan menyentuh persistence.
6. Dokumentasi, spesifikasi, dan ADR modul yang relevan.

## Aturan AI

1. Pertahankan boundary Modular Monolith / DDD-lite.
2. Jangan menciptakan arsitektur project-wide baru hanya untuk satu fitur.
3. Jangan menempatkan business behavior di `core/`, `utils/`, HTTP route, atau ORM model hanya karena lebih mudah.
4. Jangan mengimpor internal infrastructure lintas modul.
5. Utamakan pola yang sudah ada sebelum memperkenalkan abstraction baru.
6. Hindari abstraction spekulatif. Implementasikan desain paling kecil yang tetap koheren dengan requirement saat ini.
7. Setiap perubahan behavior harus memiliki test pada level paling murah yang tetap memberi keyakinan memadai.
8. Jalankan Ruff, Pyright, dan pytest sebelum menyatakan implementasi selesai.
9. Jika arsitektur atau konvensi jangka panjang berubah, tambahkan atau perbarui ADR.
10. Jika requirement baru ditemukan ketika implementasi berjalan, perbarui spec/plan terkait daripada diam-diam mengubah scope.
11. **Semua dokumentasi yang dibuat atau diperbarui oleh AI wajib menggunakan Bahasa Indonesia.**
12. Nama class, function, variable, module, command, endpoint, dan identifier source code tetap menggunakan Bahasa Inggris sesuai konvensi Python kecuali domain memang memiliki istilah khusus yang tidak tepat diterjemahkan.
13. Istilah teknis Bahasa Inggris boleh dipertahankan jika lebih presisi, tetapi penjelasan dan konteksnya harus menggunakan Bahasa Indonesia.

## Catatan Kerja Incremental

Untuk pekerjaan substansial, gunakan `docs/templates/FEATURE-SPEC.md` sebelum implementasi dan `docs/templates/CHANGE-RECORD.md` selama/setelah implementasi. Mekanisme ini membuat keputusan AI dapat ditinjau dan mencegah architecture drift yang tidak terdokumentasi.

Semua Feature Spec, Change Record, ADR, implementation note, dan dokumentasi modul harus ditulis dalam Bahasa Indonesia.

## Definition of Done

Sebuah perubahan dianggap selesai ketika behavior bekerja, test mencakup kasus penting, static checks lolos, boundary tetap valid, dampak migration/operasional terdokumentasi, dokumentasi terkait sudah tersinkronisasi, dan seluruh dokumentasi baru/perubahan menggunakan Bahasa Indonesia.
