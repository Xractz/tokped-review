# TOKPED Review Scraper

![image](https://github.com/user-attachments/assets/e67c85d5-f1cd-4172-9319-ba25c1518776)


TOKPED Review Scraper adalah program Python yang digunakan untuk mengambil data ulasan produk dari Tokopedia. Program ini menggunakan Selenium untuk mengautomasi pengambilan data dan BeautifulSoup untuk memparsing HTML. Data yang diambil meliputi nama pengguna, ulasan, media, rating, dan waktu komentar, kemudian disimpan dalam format CSV.

## Fitur

- Mengambil data ulasan produk dari Tokopedia.
- Mendukung pemrosesan semua halaman dengan mengklik tombol "Laman berikutnya" secara otomatis.
- Menyimpan hasil dalam file CSV.

## Instalasi

1. Clone repositori ini dengan cara:
    ```bash
    git clone https://github.com/Xractz/tokped-review.git
    ```
2. Buat lingkungan virtual dan aktifkan:

   ```bash
   python -m venv venv
   ```

   Aktifkan virtual environment:

   - Untuk macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

   - Untuk Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install dependencies yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

## Cara Penggunaan

1. Ubah url ulasan produk pada file `main.py`:

   ```python
    def main() -> None:
	    url = "https://www.tokopedia.com/project1945/project-1945-sunset-in-sumba-perfume-edp-parfum-unisex-100ml-2-0-e8aa9/review"
	    scraper = ReviewScraper(url)
	    scraper.run()
   ```
2. Jalankan file `main.py` dengan cara:
    ```bash
    py main.py
    ```
3. Script akan berjalan dan mulai mengambil ulasan dari produk di Tokopedia sesuai dengan URL yang telah ditentukan.
4. Setelah selesai, ulasan akan disimpan ke dalam file `tokopedia_review.csv`.
