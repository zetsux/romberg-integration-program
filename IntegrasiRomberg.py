"""
[ Praktikum 2 Komputasi Numerik C Kelompok 09 ( Implementasi Integrasi Romberg ) ]
Anggota :
- Alfa Fakhrur Rizal Zaini / 5025211214
- Andhika Lingga Mariano / 5025211161
- Kevin Nathanael Halim / 5025211140

Penjelasan Singkat :
Merupakan implementasi kode dari pencarian nilai integrasi yang merupakan nilai luasan/area yang dibatasi oleh
fungsi y(x) yang dimasukkan dengan menggunakan metode Integrasi Romberg yang merupakan hasil pengembangan dari
Integrasi Trapezoidal dengan menggunakan Richardson Extrapolation sehingga menghasilkan hasil yang jauh lebih akurat

Cara Penggunaaan :
- Memasukkan persamaan fungsi ke dalam fungsi lambda y
- Melakukan run pada kode program
- Mengisikan Derajat Error, Batas Atas, dan Batas Bawah yang diinginkan untuk memulai perhitungan integrasi
- Tabel Romberg pun akan ditampilkan beserta dengan hasil akhir integrasinya
"""

# Import library yang diperlukan
import numpy as np
import math

# Persamaan Fungsi ( y = e^x )
y = lambda x: math.exp(x)

# Pengisian derajat error yang diinginkan untuk dicapai (hasil akhir akan memiliki estimasi error kurang lebih O(n^errOrder))
print('Silahkan masukkan Derajat Error yang diinginkan (genap) : ')
errOrder = int(input())

while errOrder & 1 :
    print('Dimohon untuk memasukkan derajat error yang bernilai genap...')
    print('Silahkan masukkan Derajat Error yang diinginkan (genap) : ')
    errOrder = int(input())

# Pengisian batas atas dan bawah untuk integrasi
print('Silahkan masukkan Batas Bawah awal yang diinginkan : ')
lowerBound = int(input())
print('Silahkan masukkan Batas Atas awal yang diinginkan : ')
upperBound = int(input())
print("")

"""
    Variabel-variabel dalam fungsi
    
    a : batas bawah
    b : batas atas
    n : jumlah pias (pada Integrasi Trapezoidal)
    r : jumlah baris tabel (pada Integrasi Romberg)
    iTn : hasil Integrasi Trapezoidal dengan jumlah pias n
    iR[k, j] : hasil Integrasi Romberg dengan Richardson Extrapolation di kolom ke-(k + 1) dan baris ke-(j + 1)
"""

# Fungsi Perhitungan Integrasi Trapezoidal
def trapezoidalIntegration(n, a, b):

    tmp = a

    # Formula Integrasi Trapezoidal
    h = (b - a)/n

    # Perhitungan Integrasi Trapezoidal untuk jumlah pias n
    iTn = y(a)
    for k in range(1, n):
        tmp += h
        iTn += (2*y(tmp))

    return ((iTn + y(b))*h)/2

# Fungsi Perhitungan Integrasi Romberg
def rombergIntegration(r, a, b):

    iR = np.zeros((r, r))
    for k in range(0, r):
        # Perhitungan Integrasi Trapezoidal untuk jumlah pias 2^k
        iR[k, 0] = trapezoidalIntegration(2**k, a, b)

        # Perhitungan Integrasi Romberg dengan Rekursi
        for j in range(0, k):
            iR[k, j+1] = ((4**(j+1) * iR[k, j]) - iR[k-1, j]) / (4**(j+1) - 1)

        # Menampilkan hasil baris ke-(k + 1) dari tabel Romberg
        print(iR[k, 0:k+1])

    # Mengambil hasil akhir dari diagonal paling bawah kanan
    res = iR[tableRow - 1, tableRow - 1]
    print(f"\nHasil Akhir : {res}")

# Jumlah baris pada Tabel Romberg
tableRow = int(errOrder/2)

# Mengeluarkan Tabel Romberg
print("Tabel Romberg :\n")
iter = 1
while (iter <= tableRow) :
    print(f"\tO(n^{iter*2})", end = "\t")
    iter += 1
print("")

# Mengeluarkan batas tabel
for row in range(0, iter) :
    print(f"━━━━━━━━━━", end = "")
print("")

# Memanggil fungsi Integrasi Romberg
rombergIntegration(tableRow, lowerBound, upperBound)