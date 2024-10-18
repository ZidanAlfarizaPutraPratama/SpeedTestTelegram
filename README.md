```markdown
# SpeedTest Telegram Bot

Bot Telegram ini memungkinkan pengguna untuk menguji kecepatan internet mereka dengan mudah. Bot akan memeriksa apakah pengguna telah bergabung dengan channel tertentu sebelum memberikan hasil pengujian.

## Fitur

- Mengukur kecepatan download dan upload.
- Memeriksa status keanggotaan pengguna di channel Telegram.
- Mendaftar pengguna ke database MongoDB.

## Prerequisites

- Python 3.7 atau yang lebih baru
- MongoDB Atlas (atau server MongoDB lokal)
- Token bot Telegram

## Instalasi

1. **Clone Repositori:**

   ```bash
   git clone https://github.com/ZidanAlfarizaPutraPratama/SpeedTestTelegram.git
   cd SpeedTestTelegram
   ```

2. **Buat dan Aktifkan Lingkungan Virtual:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Untuk macOS/Linux
   # venv\Scripts\activate  # Untuk Windows
   ```

3. **Instal Dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Siapkan File `.env`:**

   Buat file bernama `.env` di direktori proyek dan tambahkan variabel berikut:

   ```plaintext
   TELEGRAM_TOKEN=your_telegram_token
   GROUP_CHAT_ID=your_group_chat_id
   CHAT_ID=your_channel_username  # Ganti dengan username channel Anda
   MONGODB_URI=your_mongodb_uri
   ```

## Menjalankan Bot Secara Lokal

Setelah semua pengaturan selesai, jalankan bot dengan perintah:

```bash
python your_script.py  # Ganti dengan nama file skrip Python yang sesuai
```

## Cara Deploy di VPS Ubuntu 22

1. **Akses VPS:**
   Masuk ke VPS menggunakan SSH:
   ```bash
   ssh username@your_vps_ip
   ```

2. **Perbarui dan Instal Dependensi:**
   Pertama, perbarui sistem dan instal Python serta pip (jika belum terinstal):
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo apt install python3 python3-pip python3-venv git
   ```

3. **Clone Repositori:**
   Jika proyek kamu sudah di-host di GitHub, kamu bisa meng-clone repositorinya:
   ```bash
   git clone https://github.com/ZidanAlfarizaPutraPratama/SpeedTestTelegram.git
   cd SpeedTestTelegram
   ```

4. **Buat Lingkungan Virtual:**
   Buat lingkungan virtual untuk proyek:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Instal Dependensi:**
   Instal semua dependensi yang tercantum dalam `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

6. **Siapkan File `.env`:**
   Buat file `.env` di dalam direktori proyekmu dan isi dengan variabel yang diperlukan.

7. **Jalankan Bot:**
   Setelah semuanya siap, jalankan bot:
   ```bash
   python your_script.py  # Ganti dengan nama file skrip Python yang sesuai
   ```

8. **Menjalankan Bot di Background (Optional):**
   Agar bot tetap berjalan di background, kamu bisa menggunakan `nohup` atau `screen`:
   - **Menggunakan `nohup`:**
     ```bash
     nohup python your_script.py &
     ```
   - **Menggunakan `screen`:**
     ```bash
     screen -S mybot
     python your_script.py
     # Tekan Ctrl+A, lalu D untuk mendetach dari screen
     ```

9. **Memastikan Bot Berjalan:**
   Untuk memastikan bot berjalan, kamu bisa memeriksa proses yang sedang berjalan:
   ```bash
   ps aux | grep python
   ```

10. **Menghentikan Bot:**
    Jika perlu menghentikan bot, kamu bisa mencari PID (Process ID) dan menghentikannya:
    ```bash
    kill <PID>
    ```

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

## Kontak

Jika ada pertanyaan atau saran, silakan hubungi [Zidan Alfariza](mailto:zidanalfariza@gmail.com).
```
