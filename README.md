
# Django Modular App - Product Module

## Deskripsi
Aplikasi ini adalah contoh implementasi **Django Modular System** dengan modul `Product` sederhana. Aplikasi dilengkapi dengan autentikasi, otorisasi berbasis grup (manager, user, public), dan sistem modular yang memungkinkan penambahan modul baru secara fleksibel.

## Fitur Utama
- Login/logout dengan otentikasi standar Django.
- Role-based access control:
  - `manager`: dapat Add, Edit, Delete produk.
  - `user`: hanya Add dan Edit produk.
  - `public`: hanya dapat melihat daftar produk.
- Modul `Product`:
  - CRUD produk (nama, barcode, harga, stok).
  - Tampilan menggunakan Bootstrap 5.
  - Delete produk menggunakan konfirmasi modal popup.
- Modular engine:
  - Modul terdaftar di tabel `Module`.
  - Hanya modul aktif yang ditampilkan dan dijalankan.
- ERD dan Flowchart disertakan.
- Role-based username & Password:
  - username: `manager`, password : hashmicro123
  - username: `user`: hashmicro123, password : hashmicro123
  - username: `public`: hashmicro123, password : hashmicro123

## Struktur Project
django-developer-test/
├── modular_project/
│   ├── example_module/               # Aplikasi modular "Product"
│   ├── modular_engine/               # Engine utama (core app)
│   └── templates/
│       ├── base.html                 # Template dasar Bootstrap
│       └── example_module/           # Template khusus untuk example_module
├── docs/                            # Folder untuk dokumentasi gambar, flowchart, ERD, dll
│   ├── ERD.png
│   ├── Flowchart-Engine-Module.png
│   └── Flowchart-Example-Module.png
├── venv/                           # Virtual environment (sebaiknya di .gitignore)
├── db.sqlite3                      # Database SQLite (jika memang pakai SQLite lokal)
├── manage.py
├── README.md
└── requirements.txt

## Instalasi & Menjalankan Aplikasi
1. **Clone Repository**
   ```bash
   git clone <repo-url>
   cd django-developer-test
   ```

2. **Aktifkan Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instal Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrasi Database**
   ```bash
   python manage.py migrate
   ```

5. **Buat Superuser (opsional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Jalankan Server**
   ```bash
   python manage.py runserver
   ```

## Informasi Tambahan
- Untuk menambah modul baru, cukup buat app baru dan daftarkan di `Module` table.
- Kelompok pengguna (`Group`) bisa ditambahkan via admin:
  - Manager, User, Public
- Pastikan setiap view menggunakan `@group_required` agar modul dapat dikendalikan per grup.

## Penulis
Dibuat untuk keperluan **Technical Test Django Developer**, oleh [Nama Kamu].
