# Romberg Integration Program

## Description
A program that implements Romberg Integration to calculate Integration

## Integrasi Romberg and it's superiority to Trapezoidal Integration
Integrasi Romberg merupakan aplikasi dari aturan Integrasi Trapezoidal yang dikembangkan lebih lanjut menggunakan perluasan dengan Richardson Extrapolation untuk memperoleh nilai integrasi yang lebih baik dan akurat. Metode ini dipergunakan dikarenakan Integrasi Trapezoidal masih memiliki akurasi hasil yang rendah, atau dengan kata lain nilai error yang cukup besar untuk nilai integrasi besar. Maka, untuk mengatasi kekurangan dari metode Integrasi Trapezoidal tersebut, digunakanlah Richardson Extrapolation untuk mencoba mengestimasi nilai errornya untuk nantinya dikurangkan dengan hasil estimasi yang diperoleh dari Integrasi Trapezoidal sehingga akurasi yang didapatkan meningkat secara drastis. Metode ini dapat diilustrasikan dengan membuat suatu tabel bernama Tabel Romberg yang bentuk dan isinya kurang lebih sebagai berikut,

<p align="center">
  <img width="640" src="https://cdn.discordapp.com/attachments/995337235211763722/1055121117184012398/image.png" alt="Romberg Table Image">
</p>

- O(h<sup>i</sup>) : Derajat Error, nilainya berbanding terbalik dengan order/nilai pangkat dari h yakni i, dimana semakin besar pangkatnya maka semakin kecil nilai errornya
- A<sub>i</sub> : Hasil Integrasi Trapezoidal, dengan jumlah pias (n) bernilai 2<sup>(i-1)</sup>
- B<sub>i</sub>,C<sub>i</sub>,D<sub>i</sub>,E<sub>i</sub>,F<sub>i</sub>,… = R<sub>(i,2)</sub>,R<sub>(i,3)</sub>,R<sub>(i,4)</sub>,R<sub>(i,5)</sub>,R<sub>(i,6)</sub>,… : Hasil dari Integrasi Romberg menggunakan Richardson Extrapolation dengan menggunakan nilai-nilai yang telah didapatkan sebelumnya dengan formula sebagai berikut,

<p align="center">
  <img width="400" src="https://cdn.discordapp.com/attachments/995337235211763722/1055121854316154890/image.png" alt="Romberg Table Image">
</p>

Bisa dilihat dari tabel perhitungan di atas, bahwasannya tiap penerapan Richardson Extrapolation akan meningkatkan order dari derajat error/kesalahan yang didapatkan dari hasil integrasi sebanyak 2. Nantinya, estimasi integrasi yang paling akurat atau yang memiliki nilai error paling kecil adalah yang berada pada ujung kanan diagonal paling bawah dari tabel Romberg yang diperoleh menggunakan perhitungan dari nilai awal yang ada. Hasil yang didapatkan bisa memiliki nilai akurasi yang jauh lebih tinggi dikarenakan adanya pengurangan dari hasil Integrasi Trapezoidal dengan faktor error yang ada.

## Code Run Result
With the input of function f(x) = e<sup>x</sup>, the output of the code is as follows,
<p align="center">
  <img width="640" src="https://cdn.discordapp.com/attachments/995337235211763722/1055120139407859763/image.png" alt="Romberg Table Image">
</p>
