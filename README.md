# Aplikasi_Reservasi_Hotel_Sederhana
---
<br>
<h1 align="center">Praktikum Dasar-Dasar Pemograman<br> </h1>
<h2 align="center"> Aplikasi Reservasi Hotel Sederhana <br> </h2>
<p align="center">KELOMPOK A7<br></p>
---
<p align="center">
  <b>ANGGOTA KELOMPOK :</b>
</p>

| No | Nama | NIM | Tugas |
|:---:|:---|:---|:---|
| 1 | Jessica Chatarina Sinaga| 2609116016| konsep Pemograman dan Pengembangan Program |
| 2 | Firdaus Ramadhani | 2609116004 |  Pengembangan program dan Flowchart |
| 3 | Shella Nazeela Saputra| 2609116018| Laporan dan Pengembangan Program |
| 4 | Satria Aji Sastra| 2609116019 | Pengembangan Program dan Penjelasan alur di Laporan |

---

<p align="center"> Deskripsi :<br>
Program reservasi hotel menggunakan Python merupakan aplikasi sederhana yang dirancang untuk membantu proses pemesanan dan pengelolaan kamar hotel secara terkomputerisasi. Program ini memiliki beberapa fitur, seperti login pengguna dan admin, melihat daftar kamar, melakukan reservasi, serta mengelola data kamar. <br>
Adapun tujuan dari program ini adalah<br>
  
> 1.	Menghasilkan aplikasi reservasi hotel sederhana yang dapat menjalankan proses pemesanan kamar sesuai dengan fitur yang dirancang. <br>
> 2.	Memahami proses perancangan dan implementasi program untuk menyelesaikan permasalahan yang berkaitan dengan reservasi hotel. <br>
> 3.	Aplikasi dirancang sebagai program sederhana untuk memenuhi kebutuhan pembelajaran mata kuliah Dasar-Dasar Pemrograman, bukan sebagai sistem reservasi hotel komersial yang sepenuhnya terintegrasi.<br>

---

## Flowchart
1. Flowchart Menu Login <br>
> Flowchart dibawah mendeskripsikan alur bagaimana proses menu login berjalan yang dimana proses tersebut dibuat agar pengguna program bisa memiliki 2 role dengan cara memaasukkan username dan password. Selain itu terdapat dua role didalam menu login tersebut yaitu Role Admin dan Role User <br>

<img width="16384" height="16144" alt="PA DDP-Page-1 drawio" src="https://github.com/user-attachments/assets/2b4fea18-7c18-429c-a9d2-bf3dc3868b9a" /><br>

2. Flowchart Menu Admin <br>
<img width="7300" height="4802" alt="PA DDP-Page-2 drawio (1)" src="https://github.com/user-attachments/assets/6da1521b-7bf6-4ff5-b6ec-1cbf22696dc1" /><br>

> Flowchart diatas merupakan alur dari menu admin yang dimana setelah username memasukkan username dan password yang sesuai dengan akun admin, program akan menjalankan memu admin kepada pengguna. Fitur yang ada didalam menu tersebut yaitu menambah kamar, melihat daftar kamar, melihat daftar reservasi, mengubah harga dan status kamar, menghapus kamar, mengganti hotel, serta logout.<br>

3. Flowchart Menu User <br>
<img width="16384" height="8871" alt="PA DDP-Page-3 drawio" src="https://github.com/user-attachments/assets/316628f1-3ca1-4050-b262-d282ef5993ee" /><br>

> Flowchart diatas merupakan alur dari menu User yang dimana setelah username memasukkan username dan password yang sesuai dengan akun User, program akan menjalankan memu user kepada pengguna. Adapun isi menunya yaitu ,melihat daftar kamar dan harga, melakukan pemesanan kamar, melihat reservasi, membatalkan reservasi, mencetak invoice, melakukan top up saldo, mengganti hotel, dan logout.<br>
---

## Komponen yang ada di dalam program ini:

`Def` ==> Digunakan untuk membuat sebuah fungsi baru. contoh fungsi menu admin, dimana fungsi ini berisi semua opsi pilihan untuk menu admin.

`library` ==> Fitur yang sudah disediakan oleh python. Dengan import (import json, import pwinput, import prettytable, dll), fitur tersebut dipanggil untuk memproses perintah lainnya di program ini. 

Library yang ada di program ini:
 
> import json ==> Untuk membaca/ngeload, menyimpan data ke database yang sudah dibuat (data kamar, reservasi, akun) <br>
> import os ==> Khususnya os clear untuk membersihkan history program ketika telah dijalankan, bertujuan agar terminal lebih rapih dan bersih. <br>
> import pwinput ==> Untuk menyamarkan password menjadi bintang (*) ketika penginputan. <br>
> import prettytable ==> Untuk menampilkan data menjadi sebuah tabel agar terlihat lebih rapih dan mudah dibaca/lihat. <br>
> import time ==> Untuk memberikan jeda di beberapa program contohnya saat pencetakan invoice sseakan-akan pencetakan sedang diproses. <br>

`if-else` ==> Untuk membuat percabangan opsi. selain itu untuk validasi input jika tidak sesuai opsi.

`try-except` ==> Sebagai error handling ketika input tidak sesuai ketentuan dan jika menekan (ctrl + c).

`while` ==> Untuk membuat menu terus menerus berulang sampai user keluar dari aplikasi.

`for` ==> Untuk mengurutkan secara terus menerus data yang tersimpan di database (kamar, harga, tipe) sampai seluruh data terlaod/terbaca.

`print` ==> Untuk menampilkan output.


# FITUR PER-ROLE 

## FITUR MENU ROLE ADMIN <BR>
**Dibawah adalah menu dari role admin secara berurutan** <br>

<img width="252" height="161" alt="Cuplikan layar 2026-11-03 205827" src="https://github.com/user-attachments/assets/f931d502-f6c8-4f63-806d-ad9deea3d1ed" /><br>
**1. Tambah Kamar Baru**<br>
> Menu ini digunakan oleh admin untuk menambahkan data kamar baru ke dalam sistem hotel yang sedang dipilih. Admin diminta untuk memasukkan nama kamar, tipe kamar, dan harga kamar dengan validasi sistem yang memastikan input tidak kosong dan harga tidak bernilai negatif. Setelah data lengkap, kamar baru akan otomatis tersimpan dengan status "Tersedia".

**2. Lihat Semua Kamar** <br>
> Menu ini digunakan oleh admin untuk melihat daftar keseluruhan kamar yang terdaftar pada hotel yang sedang dipilih. Program akan menampilkan informasi lengkap dalam bentuk tabel yang mencakup nomor, nama kamar, tipe kamar, harga (dalam format Rupiah), dan status ketersediaan kamar tersebut.

**3. Lihat Daftar Reservasi (Semua Hotel)** <br>
> Menu ini digunakan oleh admin untuk melihat rekapitulasi seluruh data reservasi pelanggan dari semua hotel yang dikelola dalam sistem. Informasi yang ditampilkan meliputi nomor, nama customer, nama hotel tempat memesan, nomor kamar, serta tipe kamar yang dipesan dalam format tabel yang rapi.

**4. Ubah Harga dan Status Kamar** <br>
> Menu ini digunakan oleh admin untuk memperbarui informasi harga atau status ketersediaan dari kamar tertentu. Admin dapat memilih kamar berdasarkan nomor urut, lalu memasukkan harga baru atau mengubah status kamar antara "Tersedia" dan "Tidak Tersedia" sesuai kebutuhan.

**5. Hapus Data Kamar** <br>
> Menu ini digunakan oleh admin untuk menghapus data kamar yang sudah tidak aktif atau salah dari daftar hotel yang sedang dipilih. Admin memasukkan nomor urut kamar yang ingin dihapus, dan sistem akan menghapus data tersebut secara permanen dari penyimpanan.

**6. Ganti Pilihan Hotel** <br>
> Menu ini digunakan oleh admin untuk beralih atau mengganti pengelolaan ke hotel lain (seperti Hotel Aston, Hotel Mercure, atau Hotel Harris) tanpa harus keluar dari program utama.

**0. Logout** 
> Menu ini digunakan oleh admin untuk keluar dari sesi menu admin saat ini dan menghentikan perulangan program atau kembali ke halaman utama sistem.   


## FITUR MENU ROLE USER <BR>
**Dibawah adalah menu dari role user secara berurutan** <br>

<img width="300" height="275" alt="Screenshot 2026-11-03 171846" src="https://github.com/user-attachments/assets/e1f38c9b-0653-4eba-bace-394dd0bc0c4e" /> <br>
**1. Melihat Data Kamar**
> Menu ini digunakan oleh user untuk melihat daftar kamar yang tersedia di hotel yang sedang dipilih. Program akan menampilkan informasi berupa nomor kamar, nama kamar, tipe kamar, dan harga kamar. Kamar yang berstatus tidak tersedia tidak akan ditampilkan, sehingga user hanya dapat melihat kamar yang bisa dipesan.

**2. Pesan Kamar**<br>
>  Menu ini digunakan untuk melakukan pemesanan kamar hotel. User dapat memilih kamar berdasarkan daftar kamar yang tersedia. Setelah memilih kamar, program akan memeriksa saldo akun. Jika saldo tidak mencukupi, user akan diberikan pilihan untuk melakukan top up terlebih dahulu. Jika saldo mencukupi dan pemesanan dikonfirmasi, biaya kamar akan dipotong dari saldo, data reservasi disimpan, dan status kamar berubah menjadi tidak tersedia.

**3. Lihat Reservasi**<br>
> Menu ini digunakan untuk melihat riwayat reservasi yang telah dilakukan oleh user. Program akan mengambil data dari file `reservasi.json`, kemudian menampilkan reservasi berdasarkan username yang sedang login. Informasi yang ditampilkan meliputi nama hotel, nama kamar, tipe kamar, dan harga kamar.

**4. Batalkan Reservasi**<br>
> Menu ini digunakan untuk membatalkan reservasi kamar yang sudah dilakukan. User dapat melihat daftar reservasinya, kemudian memilih reservasi yang ingin dibatalkan. Setelah melakukan konfirmasi, data reservasi akan dihapus dari file reservasi.json dan status kamar akan dikembalikan menjadi tersedia sehingga dapat dipesan kembali.

**5. Cetak Invoice** <br>
> Menu ini digunakan untuk mencetak atau menampilkan invoice sebagai bukti informasi pemesanan kamar. User dapat memilih reservasi yang ingin dibuatkan invoice. Program akan menampilkan identitas tamu, informasi hotel, nama kamar, tipe kamar, biaya sewa, pajak daerah sebesar 10%, dan total tagihan yang harus dibayarkan.

**6. Top Up** <br>
> Menu ini digunakan untuk menambahkan saldo ke akun user agar dapat digunakan untuk melakukan pemesanan kamar. Program akan menampilkan saldo saat ini, kemudian meminta user memasukkan nominal top up. Nominal minimal adalah Rp100.000 dan maksimal Rp10.000.000. Setelah berhasil, saldo baru akan disimpan ke dalam file `akun.json.`

**7. Ganti Hotel** <br>
> Menu ini digunakan apabila user ingin mengganti hotel yang sedang dipilih. Program akan menampilkan tiga pilihan hotel, yaitu Hotel Aston, Hotel Mercure, dan Hotel Harris. Setelah user memilih salah satunya, tampilan menu akan diperbarui sesuai hotel yang dipilih sehingga user dapat melihat dan memesan kamar di hotel tersebut.

**8. Logout**
> Menu ini digunakan untuk keluar dari akun user. Ketika user memilih angka 0, program akan menampilkan pesan bahwa user sedang keluar dari menu, kemudian menghentikan perulangan menu user. Setelah itu, pengguna kembali ke menu awal aplikasi.

## Screenshoot Dan Penjelasan Output<br>

## Output menggunakan Akun Admin<br>


<img width="496" height="202" alt="Screenshot 2026-11-03 193309" src="https://github.com/user-attachments/assets/a57dc0db-6b83-4f45-b173-6fac77775dac" />

Ini adalah Output pertama saat Aplikasi di buka yang menampilkan 3 menu yaitu menu Login,Registrasi Akun,Keluar Aplikasi<br>

<img width="449" height="381" alt="Screenshot 2026-11-02 224759" src="https://github.com/user-attachments/assets/2e055fca-84cb-4cbd-9934-07e2bd5e0d57" /> <br>

Ini Adalah Output saat memilih menu 1/Login sistem akan meminta input ussername dan password, lalu setelah selesai sistem akan meminta kita memilih salah satu hotel<br>

<img width="472" height="475" alt="Screenshot 2026-11-02 225456" src="https://github.com/user-attachments/assets/27133543-3477-4e47-bf4e-df04cbd0196d" /><br>

ini adalah output setelah memilih hotel, maka akan ada menu admin<br>

<img width="745" height="494" alt="Screenshot 2026-11-02 230251" src="https://github.com/user-attachments/assets/0ce74da0-2c18-46bf-895f-f592669081b1" /><br>

ini adalah output saat memilih menu Tambah Kamar di menu Admin, saya menginput 2 kamar disini<br>

<img width="685" height="566" alt="Screenshot 2026-11-02 230802" src="https://github.com/user-attachments/assets/b48ea780-a2de-47db-83cd-8503d38c893a" /><br>

ini adalah output dari menu 2 di menu Admin yaitu Lihat Semua Kamar jadi disini semua daftar kamar akan di tampilkan menggunakan "PrettyTable"<br>

<img width="671" height="456" alt="Screenshot 2026-11-02 231048" src="https://github.com/user-attachments/assets/b051e2f6-fb96-41b5-b0eb-9a60d008cca4" /><br>

ini adalah output dari menu Admin ke 3 yaitu melihat data resevasi customer di semua hotel jadi jika ada customer yang telah reservasi akan diatmpillkan datanya di menu 3<br>

<img width="723" height="662" alt="Screenshot 2026-11-02 231420" src="https://github.com/user-attachments/assets/03ed1c0b-275d-4946-ac53-e37bdca31a89" /> <br>

ini adalah Output dari menu ke 4 yaitu untuk mengedit Harga dan Status Kamar<br>

<img width="694" height="697" alt="Screenshot 2026-11-02 231624" src="https://github.com/user-attachments/assets/86bd82c9-3d59-4dfb-93cd-4a597edce775" /><br>

ini adalah output menu ke 5 di menu admin yaitu untuk menghapus Data Kamar<br>

<img width="540" height="462" alt="Screenshot 2026-11-02 231802" src="https://github.com/user-attachments/assets/9a69f093-e653-4930-baa1-5b2eb91ce6db" /><br>

ini adalah Output menu ke 6 di menu Admin yaitu untuk mengganti pilihan hotel, misalkan Admin mau edit atau tambah kamar di hotel lain<br>

<img width="528" height="606" alt="Screenshot 2026-11-02 232019" src="https://github.com/user-attachments/assets/ec6c5f52-5a3d-471e-a484-dd5bb58ff742" /><br>

ini adalah Output menu 0/Logout saat menu ini dipilih maka akan kembali ke menu pertama.<br>

# Output Menggunakan Akun User/Customer<br>

<img width="588" height="395" alt="Screenshot 2026-11-02 233030" src="https://github.com/user-attachments/assets/c8afcd8f-aa36-4d0c-8005-4a03b0e80e8b" /><br>

Pertama registrasi akun dulu di menu 2 untuk membuat aku Costomer/User <br>

<img width="483" height="539" alt="Screenshot 2026-11-02 233254" src="https://github.com/user-attachments/assets/f2e7134b-414e-46dc-a217-9bfd5ffc131f" /><br>

ini adalah output akun User setelah Login, Yaitu User dipersilahkan memilih hotel yang ingin ia Reservasi<br>

<img width="410" height="349" alt="Screenshot 2026-11-03 071257" src="https://github.com/user-attachments/assets/8402e82c-f53e-41a6-9dc7-ae03c2f6ff97" /><br>

ini adalah menu user setelah memilih Hotel yang ingin di Reservasi<br>

<img width="634" height="284" alt="Screenshot 2026-11-03 071454" src="https://github.com/user-attachments/assets/11add7c7-8d6a-4df7-b642-9a57de0cfd6f" /><br>

ini adalah output dari menu lihat daftar Kamar<br>

<img width="915" height="816" alt="Screenshot 2026-11-03 071756" src="https://github.com/user-attachments/assets/9379d256-b037-4dd6-8549-a08b4758d864" /><br>

ini adalah output dari menu pesan kamar dan karena saldo user RP0 maka harus TOPUP dahulu TOPUP ini juga bisa di lakukan di menu 6.Topup <br>

<img width="686" height="293" alt="Screenshot 2026-11-03 072132" src="https://github.com/user-attachments/assets/f9750942-0f58-4d4c-8ecf-c9c17f04453e" /><br>

ini adalah Output menu 3 yaitu untuk melihat riwayat Reservasi yang di tampilkan menggunakan PrettyTable agar mudah di baca user<br>

<img width="745" height="808" alt="Screenshot 2026-11-03 072722" src="https://github.com/user-attachments/assets/cec998e0-f266-4488-afe0-95e2742a19b1" /><br>

ini adalah output menu ke 5 untuk menampilkan Struk Pembayaran/Invoice <br>

<img width="906" height="354" alt="Screenshot 2026-11-03 072912" src="https://github.com/user-attachments/assets/723c5a6a-e1d1-4bef-8f23-64eb7f1ce289" /><br>

ini adalah output dari menu Topup Saldo<br>

<img width="732" height="326" alt="Screenshot 2026-11-03 073033" src="https://github.com/user-attachments/assets/fa34025f-3d55-4301-97d9-7d707de95861" /><br>

ini adalah tampilan dari menu untuk Membatalkan Reservasi<br>

<img width="350" height="155" alt="Screenshot 2026-11-03 073214" src="https://github.com/user-attachments/assets/0252ace0-4bca-43c8-ab6d-446fd141ce62" /><br>

ini adalah menu User yaitu Ganti Hotel,jadi User bisa Ganti Hotel jika ia berubah pikiran dari Hotel Aston ingin pindah ke Mercure atau Harris<br>

<img width="471" height="596" alt="Screenshot 2026-11-03 073516" src="https://github.com/user-attachments/assets/794a1f9e-89eb-4399-8194-c2dfa7808f24" /><br>

ini adalah Output menu terakhir user yaitu Logout keluar dari menu User dan kembali ke menu awal menu Login<br>

<img width="525" height="238" alt="Screenshot 2026-11-03 073713" src="https://github.com/user-attachments/assets/9c3ff36a-bfb4-4394-b4c2-9176c0c6f68b" /><br>

ini adalah Output menu terakhir Login yaitu Keluar Aplikasi<br>





