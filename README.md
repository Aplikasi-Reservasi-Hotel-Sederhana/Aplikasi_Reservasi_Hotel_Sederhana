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
<img width="502" height="201" alt="Screenshot 2026-11-02 224211" src="https://github.com/user-attachments/assets/3c1895aa-69b1-4df8-9095-9f1a11c0d1ec" <br>

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

## Screenshoot Dan Penjelasan Kode Program<br>

## Kode Program pada Akun Admin<br>
<img width="377" height="409" alt="Cuplikan layar 2026-11-03 160221" src="https://github.com/user-attachments/assets/c27ab50f-4a79-4012-af98-66635cd94120" /><br>
Kode berikut mendefinisikan sebuah fungsi untuk menampilkan dan mengelola Menu Admin dalam sistem manajemen hotel.<br>
Kode tersebut diawali dengan memanggil fungsi pilih_hotel() untuk menentukan hotel mana yang sedang dikelola.<br>
Setelah memilih hotel yang ingin dikelola, dilanjutkan dengan menampilkan beberapa menu yang ada pada menu admin. <br>
Menggunakan Menu Berulang (while True) agar program menampilkan antarmuka pilihan menu berbasis teks secara terus-menerus hingga admin memilih untuk keluar<br>
<br>
Pilihan 1 untuk menambahkan kamar<br>
Pilihan 2 untuk menampilkan kamar<br>
Pilihan 3 untuk melihat reservasi<br>
Pilihan 4 untuk mengubah informasi kamar<br>
Pilihan 5 untuk menghapus kamar<br>
Pilihan 6 untuk memilih hotel lain<br>
Pilihan 0 untuk keluar  dari menu admin<br>
<br>
Lalu terdapat validasi dan penanganan error dengan memastikan bahwa input harus berupa angka serta mencegah program berhenti mendadak jika menekan tombol ctrl + C<br>
<br>
<img width="391" height="446" alt="Cuplikan layar 2026-11-03 155809" src="https://github.com/user-attachments/assets/215f1d66-f572-4da1-91ab-11769d284998" /><br>
Menu yang pertama adalah menambahkan kamar, dalam menu ini terdapat komponen utama yaitu:<br>
Pemuatan Data -> Memanggil fungsi muat_data_kamar() untuk mengambil data kamar yang sudah ada sebelumnya.<br>
Input Nama Kamar (while True) -> Meminta input nama kamar (contoh: A101) dengan validasi agar tidak boleh dikosongkan.<br>
Input Tipe Kamar (while True) -> Meminta input tipe kamar (contoh: Exclusive/Deluxe/Standard) dengan validasi agar tidak boleh dikosongkan.<br>
Input Harga Kamar (while True & try-except) -> Meminta input harga kamar berupa angka, memastikan nilainya tidak negatif, dan menangani error jika input bukan angka (ValueError).<br>
Setelah pada kompenen utama, terdapat penyimpanan data<br>
Mengemas data baru ke dalam dictionary kamar_baru dengan status default "Tersedia". Lalu, data baru tersebut masuk dalam list hotel yang bersangkutan, perubahan data menuju ke penyimpanan melalui fungsi simpan_data_kamar(data) dan menampilkan pesan sukses.<br>
<br>
<img width="384" height="348" alt="Cuplikan layar 2026-11-03 201039" src="https://github.com/user-attachments/assets/78368ade-063a-4f61-a205-586b457a7390" />
<br>
Menu kedua adalah menampilkan kamar, terdapat komponen utama yaitu:
Pemuatan & Pengecekan Data -> Memuat data kamar dengan fungsi muat_data_kamar(). Jika data kamar pada hotel tersebut kosong, program akan mencetak informasi bahwa belum ada kamar dan mengembalikan nilai False.<br>
Pembuatan Tabel (PrettyTable) -> Membuat objek tabel dengan kolom: No, Nama Kamar, Tipe Kamar, Harga, dan Status.<br>
Mengatur perataan teks (alignment) -> rata kiri untuk Nama dan Tipe Kamar, rata kanan untuk Harga, serta rata tengah untuk Status.   Memasukkan Data ke Tabel -> Melakukan perulangan (for) untuk mengambil setiap data kamar, memformat harga menjadi format mata uang Rupiah, lalu memasukkannya baris per baris ke dalam tabel.<br>
Menampilkan Hasil -> Mencetak tabel ke layar dan mengembalikan nilai True jika data berhasil ditampilkan.<br>
<br>
<img width="374" height="395" alt="Cuplikan layar 2026-11-03 155937" src="https://github.com/user-attachments/assets/4635635a-fb9e-4e68-b23b-0d70d85b1241" /><br>
Menu ketiga adalah melihat reservasi, komponen utamanya adalah:<br>
Membaca File JSON (try-except) -> Membuka file yang merujuk pada FILE_RESERVASI. Jika file tidak ditemukan atau format JSON rusak, program akan menampilkan informasi bahwa belum ada data reservasi dan menghentikan fungsi.<br>
Pengecekan Data -> Jika data reservasi kosong, program akan mencetak informasi bahwa belum ada reservasi dan langsung keluar.<br>
Pembuatan Tabel (PrettyTable) -> Membuat objek tabel dengan kolom: No, Nama Customer, Hotel, Kamar, dan Tipe.<br>
Mengatur perataan teks (alignment) ke sebelah kiri untuk seluruh kolom agar mudah dibaca.<br>
Memasukkan Data ke Tabel -> Melakukan perulangan (for) untuk mengambil setiap data reservasi, mengekstrak informasi detail (nama pelanggan, nama hotel, kamar, dan tipe), lalu memasukkannya baris per baris ke dalam tabel.<br>
Menampilkan Hasil -> Mencetak tabel lengkap berisi daftar reservasi ke layar.<br>
<br>
<img width="416" height="445" alt="Cuplikan layar 2026-11-03 155856" src="https://github.com/user-attachments/assets/e2200010-e05c-476e-90fb-161920d2f5da" /><br>
Menu keempat yaitu mengubah data, memiliki komponen utama yaitu :<br>
Pemuatan & Pengecekan Data -> Memuat data kamar menggunakan muat_data_kamar() dan menampilkan daftar kamar dengan tampilkan_kamar(hotel). Jika data kamar kosong, fungsi akan langsung berhenti.<br>
Pemilihan Nomor Kamar -> Meminta input nomor kamar yang ingin diubah, lalu mengubahnya menjadi indeks list (indeks = pilihan - 1) dengan validasi agar berada dalam rentang data yang ada.<br>
Pembaruan Harga Kamar -> Meminta input harga baru. Jika admin menekan Enter tanpa mengisi, harga lama akan dipertahankan, lalu memastikan input berupa angka dan bernilai positif sebelum memperbarui atribut harga pada kamar yang dipilih.<br>
Pembaruan Status Kamar -> Menampilkan status kamar saat ini. Meminta pilihan status baru (1 untuk "Tersedia", 2 untuk "Tidak Tersedia", atau menekan Enter jika ingin tetap) untuk memperbarui status kamar tersebut.<br>
<img width="419" height="83" alt="Cuplikan layar 2026-11-03 155911" src="https://github.com/user-attachments/assets/39350952-f876-4e6c-826a-8e0e8d310e2c" /><br>
Semua data baru tersebut masuk dalam list hotel yang bersangkutan, perubahan data menuju ke penyimpanan melalui fungsi simpan_data_kamar(data) serta memvalidasi semua kesalahan pada menu tersebut.<br>
<br>
<img width="388" height="274" alt="Cuplikan layar 2026-11-03 155923" src="https://github.com/user-attachments/assets/41229dab-0fb4-4609-b195-09ef79444347" /><br>
Menu kelima adalah hapus data, komponen utamanya yaitu:<br>
Pemuatan & Pengecekan Data -> Memuat data kamar menggunakan muat_data_kamar() dan menampilkan daftar kamar saat ini dengan tampilkan_kamar(hotel). Jika data kamar kosong, fungsi akan langsung berhenti (return).<br>
Pemilihan Nomor Kamar -> Meminta input nomor kamar yang ingin dihapus, di mana pengguna dapat memasukkan angka 0 jika ingin membatalkan proses.<br>
Proses Penghapusan & Penyimpanan -> Mengonversi pilihan nomor kamar menjadi indeks list (indeks = pilihan - 1).<br>
Jika nomor kamar valid, data kamar dihapus dari list menggunakan metode .pop(indeks).<br>
Menyimpan kembali data yang telah diperbarui ke penyimpanan melalui fungsi simpan_data_kamar(data) serta mencetak pesan sukses.<br>
Penanganan Kesalahan (try-except) -> Menangani error jika pengguna memasukkan input selain angka (seperti huruf atau simbol) melalui blok ValueError.
<br>
<img width="373" height="244" alt="Cuplikan layar 2026-11-03 160156" src="https://github.com/user-attachments/assets/38f3ccdd-bb8a-4427-b44d-655b4832e988" /><br>
Menu keenam adalah ganti pilihan hotel, komponennya adalah:<br>
Menu Pilihan Hotel (while True) -> Menampilkan daftar pilihan hotel (Hotel Aston, Hotel Mercure, dan Hotel Harris) secara berulang di dalam perulangan tak terbatas hingga mendapatkan input yang valid.<br>
Validasi Input Kosong -> Memeriksa apakah input dari pengguna kosong. Jika kosong, program akan mencetak pesan peringatan dan mengulang perulangan (continue).<br>
Pengembalian Nilai (Return Value) -> Jika memilih 1, fungsi mengembalikan string "Aston".   Jika memilih 2, fungsi mengembalikan string "Mercure".   Jika memilih 3, fungsi mengembalikan string "Harris".<br>
Validasi Pilihan Tidak Valid -> Jika pengguna memasukkan angka di luar rentang 1 sampai 3, program akan menampilkan pesan peringatan agar memasukkan angka yang sesuai.<br>
<br>
<img width="317" height="32" alt="Cuplikan layar 2026-11-03 203958" src="https://github.com/user-attachments/assets/8c8c3418-de0a-40d6-af48-b5817f7dd80a" /><br>
Terakhir ada menu 0, yang dapat digunakan jika admin ingin logout.<br>








