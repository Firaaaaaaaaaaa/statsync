# StatSync

StatSync adalah aplikasi berbasis web yang membantu proses ekstraksi dan pengelolaan data dari Berita Resmi Statistik (BRS) BPS Jatim. Aplikasi ini dirancang untuk mempermudah pengguna dalam mengonversi dokumen BRS menjadi format Excel.

## 📌 Fitur Utama
### Admin:
- Dashboard
- Manage User
- Log activity

### User:
- Dashboard
- Ekstraksi BRS to Excel
- Rekapitulasi

## 🚀 Cara Menjalankan Proyek
1. **Clone repository ini:**  
    Karena hanya folder statsync yang ada di GitHub, pastikan anda meng-clone langsung ke dalam folder kerja yang diinginkan:
     ```sh
     git clone https://github.com/Firaaaaaaaaaaa/statsync.git
     cd statsync
     ```

2. **Buat dan Aktifkan Virtual Environment:**  
    Di luar folder statsync (di dalam folder kerja yang anda inginkan), buat dan aktifkan virtual environment.

    ### Untuk Windows (Git Bash, CMD, atau PowerShell):
     ```sh
     python -m venv ../envdjango
     ../envdjango/Scripts/activate
     ```

    ### Untuk Mac/Linux (Terminal):
     ```sh
     python3 -m venv ../envdjango
     source ../envdjango/bin/activate
     ```

    Jika berhasil, terminal akan menampilkan (envdjango) di awal setiap baris, menandakan bahwa virtual environment telah aktif.

3. **Install Depedensi**  
    Setelah virtual environment aktif, instal semua library yang dibutuhkan dengan:
     ```sh
     pip install -r requirements.txt
     ```

4. **Konfigurasi Database**  
    Jika proyek menggunakan database, jalankan perintah berikut untuk menerapkan skema database:
     ```sh
     python manage.py makemigrations
     python manage.py migrate
     ```

    📌 Penjelasan:  
    Perintah ini akan membuat tabel-tabel yang diperlukan dalam database berdasarkan model Django.

5. **Jalankan Server Django**  
    Setelah konfigurasi selesai, jalankan server lokal dengan:
     ```sh
     python manage.py runserver
     ```
     
    Jika server berjalan dengan baik, akan muncul output seperti ini:
     ```
     Watching for file changes with StatReloader
     Performing system checks...
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.
     ```

    🚀 Sekarang, buka browser dan kunjungi http://127.0.0.1:8000/ untuk melihat proyek berjalan.

## 🛠 Teknologi yang Digunakan
- Django (Python) - Backend utama
- Bootstrap - Frontend styling
- Pandas - Ekstraksi
- mySQL - Database

Jika ada pertanyaan atau kendala, silakan hubungi pengembang proyek ini. 🚀

## Struktur Folder Proyek
```
Folder_Kerja_Anda/
│── envdjango/         # Virtual environment (tidak masuk GitHub)
│── statsync/         # Folder utama proyek (masuk GitHub)
│   │── manage.py     # File utama Django
│   │── requirements.txt # Daftar dependensi
│   │── README.md     # Dokumentasi proyek
│   └── ...          # File dan folder lainnya
```