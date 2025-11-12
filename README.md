# Romberg Integration Calculator

Program untuk menghitung estimasi nilai integral numerik menggunakan metode Romberg Integration dengan visualisasi tabel segitiga Romberg.

---

## Deskripsi

Romberg Integration adalah metode numerik untuk menghitung integral tentu yang menggunakan ekstrapolasi Richardson untuk meningkatkan akurasi dari metode Trapezoidal Rule. Metode ini menghasilkan tabel segitiga yang berisi aproksimasi integral dengan tingkat akurasi yang semakin meningkat.

### Algoritma

Program ini mengimplementasikan algoritma Romberg dengan:

- **Level minimal**: 3 (R₀,₀ sampai R₂,₂)
- **Level maksimal**: 10 (dapat disesuaikan)
- **Toleransi konvergensi**: 1×10⁻¹⁰
- **Formula ekstrapolasi**: R(n,m) = R(n,m-1) + [R(n,m-1) - R(n-1,m-1)] / (4^m - 1)

---

## Fitur

### 1. Tiga Mode Operasi

#### Mode 1: Integral Trigonometri

Menghitung integral dari fungsi kosinus:

```
∫₀^(π/2) cos(x) dx
```

**Hasil analitik**: 1.0

#### Mode 2: Integral Polinomial

Menghitung integral dari fungsi kuadrat:

```
∫₀¹ x² dx
```

**Hasil analitik**: 0.333333...

#### Mode 3: Input Custom

Pengguna dapat memasukkan fungsi dan batas integral sendiri dengan sintaks Python.

### 2. Tabel Romberg Segitiga

Program menampilkan tabel segitiga lengkap yang memvisualisasikan proses konvergensi Romberg:

```
R(n,m)      m=0             m=1             m=2             m=3
=======================================================================
n=0         0.7853981634
n=1         0.9480594220    1.0087662340
n=2         0.9871158010    1.0001095838    0.9998430220
n=3         0.9967851718    1.0000068615    0.9999998988    1.0000001659
```

### 3. Presisi Tinggi

Hasil integral ditampilkan dengan 15 digit desimal untuk akurasi maksimal.

---

## Instalasi

### Prasyarat

- Python 3.7 atau lebih baru
- pip (Python package manager)

### Langkah Instalasi

1. Clone atau download repository ini:

```bash
git clone <repository-url>
cd "tugas integral"
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

atau install manual:

```bash
pip install numpy
```

---

## Penggunaan

### Menjalankan Program

Jalankan program dengan perintah:

```bash
python main.py
```

### Contoh Interaksi

#### Contoh 1: Menghitung cos(x)

```
==================================================
ROMBERG INTEGRATION
==================================================
1. cos(x) dari 0 sampai pi/2
2. x^2 dari 0 sampai 1
3. Input sendiri
==================================================
Pilih opsi (1/2/3): 1
==================================================
Menghitung integral: cos(x)
Batas integrasi: 0 sampai π/2
==================================================

Tabel Romberg Segitiga:
...

Hasil integral: 1.000000000000000
==================================================
```

#### Contoh 2: Menghitung x²

```
Pilih opsi (1/2/3): 2
==================================================
Menghitung integral: x^2
Batas integrasi: 0 sampai 1
==================================================

Tabel Romberg Segitiga:
...

Hasil integral: 0.333333333333333
==================================================
```

#### Contoh 3: Input Custom

```
Pilih opsi (1/2/3): 3
Masukkan fungsi (gunakan x sebagai variabel, contoh: x**2, np.sin(x)): x**3 + 2*x
Masukkan batas bawah (a): 0
Masukkan batas atas (b): 2
==================================================
Menghitung integral: x**3 + 2*x
Batas integrasi: 0 sampai 2
==================================================

Tabel Romberg Segitiga:
...

Hasil integral: 8.000000000000000
==================================================
```

### Sintaks Fungsi untuk Mode Custom

Saat menggunakan mode 3 (input custom), gunakan sintaks Python standar:

| Operasi      | Sintaks     | Contoh          |
| ------------ | ----------- | --------------- |
| Pangkat      | `**`        | `x**2`, `x**3`  |
| Perkalian    | `*`         | `2*x`, `3*x**2` |
| Pembagian    | `/`         | `x/2`, `1/x`    |
| Sinus        | `np.sin()`  | `np.sin(x)`     |
| Kosinus      | `np.cos()`  | `np.cos(x)`     |
| Eksponensial | `np.exp()`  | `np.exp(x)`     |
| Logaritma    | `np.log()`  | `np.log(x)`     |
| Akar kuadrat | `np.sqrt()` | `np.sqrt(x)`    |

**Contoh fungsi kompleks**:

- `x**2 + 3*x + 1`
- `np.sin(x) + np.cos(x)`
- `np.exp(-x**2)`
- `1/(1 + x**2)`

---

## Struktur Project

```
tugas integral/
│
├── main.py              # File program utama
├── requirements.txt     # Daftar dependencies
└── README.md           # Dokumentasi (file ini)
```

---

## Penjelasan Kode

### Fungsi Utama

#### `romberg_integration(f, a, b, max_level=10, tol=1e-10)`

Fungsi utama yang mengimplementasikan algoritma Romberg.

**Parameter**:

- `f`: Fungsi yang akan diintegralkan
- `a`: Batas bawah integral
- `b`: Batas atas integral
- `max_level`: Level maksimal iterasi (default: 10)
- `tol`: Toleransi konvergensi (default: 1×10⁻¹⁰)

**Return**:

- `R`: Matriks tabel Romberg
- `result`: Nilai integral hasil akhir

#### `print_romberg_table(R)`

Menampilkan tabel Romberg dalam format segitiga.

**Parameter**:

- `R`: Matriks numpy berisi nilai-nilai Romberg

#### `integral_1(x)` dan `integral_2(x)`

Fungsi-fungsi hardcoded untuk soal integral yang telah ditentukan.

#### `main()`

Fungsi main yang mengatur alur program dan interaksi dengan pengguna.

---

## Teori Matematika

### Metode Trapezoidal

Basis dari Romberg Integration adalah Trapezoidal Rule:

```
T(h) = (h/2) × [f(a) + 2∑f(xᵢ) + f(b)]
```

### Ekstrapolasi Richardson

Romberg menggunakan ekstrapolasi untuk meningkatkan akurasi:

```
R(n,m) = R(n,m-1) + [R(n,m-1) - R(n-1,m-1)] / (4^m - 1)
```

Dimana:

- `R(n,0)` adalah hasil Trapezoidal Rule dengan 2ⁿ subinterval
- `R(n,m)` adalah aproksimasi dengan order error O(h^(2m+2))

### Konvergensi

Program berhenti ketika:

1. Mencapai level maksimal, atau
2. |R(n,n) - R(n-1,n-1)| < toleransi

---

## Dependencies

| Package | Versi   | Kegunaan                               |
| ------- | ------- | -------------------------------------- |
| numpy   | ≥1.24.0 | Komputasi numerik dan array operations |

---

## Verifikasi Hasil

### Integral 1: cos(x) dari 0 sampai π/2

**Solusi analitik**:

```
∫₀^(π/2) cos(x) dx = [sin(x)]₀^(π/2) = sin(π/2) - sin(0) = 1 - 0 = 1
```

**Hasil program**: ~1.000000000000000

### Integral 2: x² dari 0 sampai 1

**Solusi analitik**:

```
∫₀¹ x² dx = [x³/3]₀¹ = 1/3 - 0 = 0.333333...
```

**Hasil program**: ~0.333333333333333

---

## Kelebihan Metode Romberg

1. **Konvergensi cepat**: Order error meningkat secara kuadratik dengan setiap level
2. **Efisien**: Memanfaatkan hasil perhitungan sebelumnya
3. **Akurat**: Dapat mencapai presisi mesin dengan iterasi relatif sedikit
4. **Adaptif**: Dapat berhenti saat mencapai toleransi yang diinginkan

---

## Batasan

1. Fungsi harus kontinu dan smooth pada interval integrasi
2. Tidak cocok untuk fungsi dengan singularitas atau diskontinuitas
3. Memerlukan evaluasi fungsi yang cukup banyak untuk konvergensi
4. Untuk fungsi oscilatori dengan frekuensi tinggi, mungkin memerlukan level yang lebih tinggi

---

## Lisensi

Project ini dibuat untuk keperluan akademis.

---

## Referensi

1. Burden, R. L., & Faires, J. D. (2010). _Numerical Analysis_ (9th ed.). Brooks/Cole.
2. Romberg, W. (1955). "Vereinfachte numerische Integration". _Det Kongelige Norske Videnskabers Selskab Forhandlinger_, 28(7), 30-36.
3. NumPy Documentation: https://numpy.org/doc/

---

## Kontributor

- Universitas Gadjah Mada
- Mata Kuliah: Metode Numerik / Komputasi Numerik

---

**Catatan**: Program ini telah diuji dengan Python 3.7+ dan NumPy 1.24.0+
