# Panduan Metrik Evaluasi: Mengapa Kita Menggunakan Average Precision (AP)?

Repositori ini menjelaskan pemilihan metrik evaluasi model machine learning untuk kasus data yang sangat tidak seimbang (*imbalanced dataset*), seperti pada prediksi klaim asuransi perjalanan. 

Untuk memahami mengapa **Average Precision (AP)** dipilih, mari kita bedah kelemahan metrik lainnya menggunakan contoh kasus nyata.

---

## Konteks Data Simulasi (Total 5 Nasabah)
Misalkan kita memiliki data ril dari 5 nasabah, di mana **hanya 1 orang yang beneran mengajukan klaim (Nasabah A)**. Sisanya aman.
* **Kelas Positif (1):** Nasabah A (Beneran Klaim)
* **Kelas Negatif (0):** Nasabah B, C, D, E (Tidak Klaim)

---

## 1. RECALL: Mengapa Berbahaya Jika Berdiri Sendiri?

Recall hanya peduli: *"Dari semua orang yang beneran klaim, berapa % yang berhasil ditebak model?"*

### Contoh Simulasi Model "Curang" (Mengejar Recall Tinggi):
Model memprediksi **SEMUA (5 nasabah)** akan mengajukan klaim demi cari aman.
* **Hasil Prediksi Model:** Semua ditebak Klaim.
* **Evaluasi:** Nasabah A (yang beneran klaim) sukses ketangkap oleh model.
* **Skor Recall:** `1.0` (100% Sempurna!)

### Mengapa Ini Gagal Secara Bisnis?
Meskipun Recall sempurna, model ini sampah. Perusahaan asuransi harus memperlakukan seluruh 5 nasabah sebagai risiko tinggi, membuang biaya operasional investigasi, dan membuat penanganan klaim menjadi tidak efisien.

## 2. PRECISION: Mengapa Berbahaya Jika Berdiri Sendiri?

Precision hanya peduli: *"Dari semua orang yang ditebak klaim oleh model, berapa % yang beneran terbukti klaim?"*

### Contoh Simulasi Model "Cari Aman" (Mengejar Precision Tinggi):
Model hanya berani menebak **1 orang saja** (Nasabah A) sebagai "Klaim" karena datanya sangat ekstrem, sedangkan 4 nasabah lainnya langsung ditebak "Tidak Klaim".
* **Hasil Prediksi Model:** Cuma Nasabah A yang ditebak Klaim.
* **Evaluasi:** Tebakan model untuk Nasabah A terbukti 100% benar.
* **Skor Precision:** `1.0` (100% Sempurna!)

### Mengapa Ini Gagal Secara Bisnis?
Jika seandainya di dunia nyata tiba-tiba Nasabah C dan D juga ikut mengajukan klaim, model ini akan buta. Model mendapatkan skor Precision sempurna hanya dengan cara "pilih-pilih toko" dan mengabaikan risiko nasabah lainnya.

---

## 3. ROC-AUC vs AVERAGE PRECISION (AP)

Kedua metrik ini lebih maju karena tidak memakai tebakan saklek, melainkan membaca **skor probabilitas** (0.0 - 1.0) untuk mengurutkan risiko nasabah. Namun, cara mereka menghukum kesalahan model sangat berbeda.

### Contoh Skenario: Ada Penyusup di Papan Atas
Model salah memprediksi dengan menaruh **Nasabah B (Tidak Klaim)** di urutan nomor 1 dengan probabilitas tertinggi, sedangkan Nasabah A (Klaim Ril) tergeser ke nomor 2.

| Nasabah | Kondisi Ril | Probabilitas dari Model | Posisi Papan Skor |
| :--- | :--- | :--- | :--- |
| Nasabah B | Tidak Klaim | **0.95** | **Urutan 1 (Penyusup/False Alarm)** |
| **Nasabah A** | **Klaim (Positif)** | **0.90** | **Urutan 2 (Target Utama)** |
| Nasabah C | Tidak Klaim | 0.30 | Urutan 3 (Benar Rendah) |
| Nasabah D | Tidak Klaim | 0.20 | Urutan 4 (Benar Rendah) |
| Nasabah E | Tidak Klaim | 0.10 | Urutan 5 (Benar Rendah) |

#### A. Cara ROC-AUC Menilai Contoh Ini (Hasil: 0.75 - "Pemaaf")
ROC-AUC melihat tabel secara makro/keseluruhan. 
* **Logika ROC-AUC:** *"Meskipun salah di urutan pertama, Nasabah A (Klaim) posisinya masih jauh lebih tinggi dibanding mayoritas data negatif lainnya (Nasabah C, D, dan E). Kerja bagus!"*
* **Kelemahan:** Skor tetap terlihat bagus (`0.75`) padahal model melakukan kesalahan fatal di kelompok risiko tertinggi (probabilitas 0.95).

#### B. Cara Average Precision (AP) Menilai Contoh Ini (Hasil: 0.50 - "Kejam")
AP hanya memelototi kesucian area probabilitas tinggi (papan atas).
* **Logika AP:** *"Kita mencari orang yang klaim, kenapa di urutan nomor 1 dengan probabilitas 95% malah diisi orang yang TIDAK KLAIM? Ini merusak sistem!"*
* **Kelebihan:** AP langsung memberikan hukuman berat. Skor AP langsung hancur menjadi `0.50` karena adanya 1 penyusup *False Positive* di posisi puncak.

---

## Kesimpulan Akhir

Berdasarkan contoh di atas, **Average Precision (AP)** adalah metrik paling jujur dan realistis untuk data *imbalanced*. AP memastikan bahwa nasabah yang diberi skor probabilitas tertinggi oleh model adalah mereka yang **beneran memiliki risiko klaim tertinggi**, tanpa toleransi terhadap salah tebak di papan atas.