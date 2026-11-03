import json
import os
import time
import pwinput
from prettytable import PrettyTable

FILE_KAMAR = "kamar.json"
FILE_RESERVASI = "reservasi.json"
FILE_AKUN = "akun.json"


def muat_data_akun():
    """Memuat data akun, jika gagal buat default sementara."""
    try:
        with open(FILE_AKUN, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data_awal = {
            "admin": {"Admin1": {"password": "iniadmin"}},
            "user": {},
        }
        with open(FILE_AKUN, "w", encoding="utf-8") as file:
            json.dump(data_awal, file, indent=4)
        return data_awal


def simpan_data_akun(data):
    with open(FILE_AKUN, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def format_rupiah(angka):
    """Fungsi bantu untuk memformat angka ke format Rupiah."""
    return f"Rp {int(angka):,}"


def muat_data_kamar():
    try:
        with open(FILE_KAMAR, "r", encoding="utf-8") as file:
            data = json.load(file)
            for hotel in ["Aston", "Mercure", "Harris"]:
                if hotel not in data:
                    data[hotel] = []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        data_awal = {"Aston": [], "Mercure": [], "Harris": []}
        simpan_data_kamar(data_awal)
        return data_awal


def simpan_data_kamar(data):
    with open(FILE_KAMAR, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def pilih_hotel():
    """Fungsi bantu untuk memilih hotel."""
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        try:
            print("\n=== PILIH HOTEL ===")
            print("1. Hotel Aston")
            print("2. Hotel Mercure")
            print("3. Hotel Harris")
            pilihan = input("Masukkan pilihan (1-3): ").strip()

            if not pilihan:
                print("[!] Pilihan tidak boleh kosong.")
                continue

            if pilihan == "1":
                return "Aston"
            elif pilihan == "2":
                return "Mercure"
            elif pilihan == "3":
                return "Harris"
            else:
                print("[!] Pilihan tidak valid. Harap masukkan angka 1 sampai 3.")
        except KeyboardInterrupt:
                print("\n[!] Jangan menekan CTRL + C!")

def registrasi():
    print("=" * 40)
    print("            REGISTRASI AKUN")
    print("=" * 40)
    akun = muat_data_akun()

    role = "user"

    while True:
        username = input("Masukkan Username Baru: ").strip()
        if not username:
            print("[!] Username tidak boleh kosong.")
            continue
        if username in akun["admin"] or username in akun["user"]:
            print(
                "[!] Username sudah terdaftar! Silakan gunakan username lain."
            )
            return
        break

    while True:
        password = pwinput.pwinput("Masukkan Password Baru: ")
        if not password.strip():
            print("[!] Password tidak boleh kosong.")
            continue

        if len(password) < 5:
            print("[!] Password terlalu pendek! Minimal harus 5 huruf/karakter.")
            continue
        break

    akun["user"][username] = {"password": password, "saldo": 0}

    simpan_data_akun(akun)
    print(f"\n[Sukses] Akun User '{username}' berhasil didaftarkan!")


def login():
    akun = muat_data_akun()
    while True:
        print("=" * 40)
        print("            SILAHKAN LOGIN")
        print("=" * 40)
        username = input("Masukkan Username : ").strip()
        if not username:
            print("[!] Username tidak boleh kosong.")
            continue

        password = pwinput.pwinput("Masukkan Password : ")
        if not password:
            print("[!] Password tidak boleh kosong.")
            continue

        if username in akun["admin"]:
            stored_pwd = akun["admin"][username]
            if isinstance(stored_pwd, dict):
                stored_pwd = stored_pwd.get("password")
            if stored_pwd == password:
                print("\nLogin Berhasil sebagai Admin")
                return "admin", username

        if username in akun["user"]:
            stored_data = akun["user"][username]
            stored_pwd = (
                stored_data.get("password")
                if isinstance(stored_data, dict)
                else stored_data
            )
            if stored_pwd == password:
                if isinstance(akun["user"][username], str):
                    akun["user"][username] = {"password": password, "saldo": 0}
                    simpan_data_akun(akun)
                print("\nLogin Berhasil sebagai User")
                return "user", username

        print("\n[!] Username atau Password salah. Silakan coba lagi.")


def topup_saldo(nama_user):
    """Menampilkan saldo saat ini dan langsung memproses top up saldo."""
    print("\n" + "=" * 40)
    print("            MENU TOPUP SALDO")
    print("=" * 40)

    akun = muat_data_akun()

    if nama_user not in akun["user"]:
        print("[!] Akun tidak ditemukan.")
        return 0

    user_data = akun["user"][nama_user]
    if isinstance(user_data, str):
        saldo_saat_ini = 0
    else:
        saldo_saat_ini = user_data.get("saldo", 0)

    print(f" Saldo Anda saat ini : {format_rupiah(saldo_saat_ini)}")
    print("-" * 40)

    while True:
        try:
            nominal = input(
                " Masukkan nominal top up (Minimal Rp100.000) (atau tekan 0 untuk batal): "
            ).strip()
            if not nominal.isdigit():
                print("[!] Harap masukkan angka yang valid.")
                continue

            nominal = int(nominal)
            if nominal == 0:
                print("[Info] Top up dibatalkan.")
                return saldo_saat_ini

            if nominal < 100000:
                print("[!] Nominal top up minimal adalah Rp100.000.")
                continue
            if nominal > 10000000:
                print("[!] Nominal top up maksimal adalah Rp10.000.000.")
                continue
            break
        except ValueError:
            print("[!] Harap masukkan angka yang valid.")
        except KeyboardInterrupt:
            print("\n[!] Jangan menekan CTRL + C!")

    if isinstance(user_data, str):
        password_lama = user_data
        akun["user"][nama_user] = {"password": password_lama, "saldo": nominal}
    else:
        akun["user"][nama_user]["saldo"] = saldo_saat_ini + nominal

    simpan_data_akun(akun)

    saldo_terkini = (
        akun["user"][nama_user]["saldo"]
        if isinstance(akun["user"][nama_user], dict)
        else nominal
    )

    print("\n[Sukses] Top up berhasil!")
    print(f" Nominal top up  : {format_rupiah(nominal)}")
    print(f" Saldo sekarang  : {format_rupiah(saldo_terkini)}")
    print("=" * 40)
    return saldo_terkini


def tampilkan_kamar(hotel):
    data = muat_data_kamar()

    print("\n" + "=" * 55)
    print(f"            DAFTAR KAMAR HOTEL {hotel.upper()}            ")
    print("=" * 55)

    if not data[hotel]:
        print("[Info] Belum ada kamar di hotel ini.")
        return False

    table = PrettyTable()
    table.field_names = [
        "No",
        "Nama Kamar",
        "Tipe Kamar",
        "Harga",
        "Status",
    ]
    table.align["Nama Kamar"] = "l"
    table.align["Tipe Kamar"] = "l"
    table.align["Harga"] = "r"
    table.align["Status"] = "c"

    for index, kamar in enumerate(data[hotel], start=1):
        harga_str = f"Rp {kamar['harga']:,}"
        table.add_row(
            [index, kamar["nama"], kamar["tipe"], harga_str, kamar["status"]]
        )

    print(table)
    return True


def tambah_tipe_kamar(hotel):
    print(f"\n=== TAMBAH TIPE KAMAR BARU DI HOTEL {hotel.upper()} = ==")
    data = muat_data_kamar()

    while True:
        nama_kamar = input("Masukkan Nama Kamar (Contoh: A101): ").strip()
        if not nama_kamar:
            print("[!] Nama kamar tidak boleh kosong.")
            continue
        break

    while True:
        tipe_kamar = input(
            "Masukkan Tipe Kamar (Contoh: Exclusive/Deluxe/Standard): "
        ).strip()
        if not tipe_kamar:
            print("[!] Tipe kamar tidak boleh kosong.")
            continue
        break

    while True:
        try:
            harga_kamar = int(input("Masukkan Harga Kamar : "))
            if harga_kamar < 0:
                print("[!] Harga kamar tidak boleh bernilai negatif.")
                continue
            break
        except ValueError:
            print("[!] INPUT HARUS BERUPA ANGKA")

    kamar_baru = {
        "nama": nama_kamar,
        "tipe": tipe_kamar,
        "harga": harga_kamar,
        "status": "Tersedia",
    }

    data[hotel].append(kamar_baru)
    simpan_data_kamar(data)
    print(
        f"\n[Sukses] Kamar '{nama_kamar}' berhasil ditambahkan ke Hotel {hotel}!"
    )


def ubah_kamar(hotel):
    print(f"\n=== UBAH HARGA & STATUS KAMAR HOTEL {hotel.upper()} ===")
    data = muat_data_kamar()
    ada_data = tampilkan_kamar(hotel)

    if not ada_data:
        return

    try:
        pilihan = int(input("Masukkan NOMOR kamar yang ingin diubah: "))
        indeks = pilihan - 1

        if 0 <= indeks < len(data[hotel]):
            kamar_terpilih = data[hotel][indeks]
            print(f"\nMengubah data untuk {kamar_terpilih['nama']}")

            harga_baru = input(
                f"Masukkan harga baru (tekan Enter jika tetap {kamar_terpilih['harga']}): "
            ).strip()
            if harga_baru:
                if harga_baru.isdigit():
                    harga_val = int(harga_baru)
                    if harga_val >= 0:
                        kamar_terpilih["harga"] = harga_val
                        print("--> Harga berhasil diperbarui.")
                    else:
                        print("[!] Harga tidak boleh negatif.")
                else:
                    print("[!] Input harga harus berupa angka.")

            print(f"Status saat ini: {kamar_terpilih['status']}")
            print("Pilih Status Baru (1. Tersedia / 2. Tidak Tersedia)")
            status_pilihan = input(
                "Masukkan pilihan (1/2 atau tekan Enter jika tetap): "
            ).strip()

            if status_pilihan == "1":
                kamar_terpilih["status"] = "Tersedia"
                print("--> Status berhasil diubah menjadi Tersedia.")
            elif status_pilihan == "2":
                kamar_terpilih["status"] = "Tidak Tersedia"
                print("--> Status berhasil diubah menjadi Tidak Tersedia.")

            simpan_data_kamar(data)
            print("\n[Sukses] Data kamar berhasil diperbarui!")
        else:
            print("\n[!] Nomor kamar tidak valid.")
    except ValueError:
        print("\n[!] Harap masukkan angka yang valid.")
    except KeyboardInterrupt:
        print("\n[!] Jangan menekan CTRL + C!")

def hapus_kamar(hotel):
    print(f"\n=== HAPUS KAMAR HOTEL {hotel.upper()} ===")
    data = muat_data_kamar()
    ada_data = tampilkan_kamar(hotel)

    if not ada_data:
        return

    try:
        pilihan = int(
            input("Masukkan NOMOR kamar yang ingin dihapus (0 untuk batal): ")
        )
        if pilihan == 0:
            return

        indeks = pilihan - 1
        if 0 <= indeks < len(data[hotel]):
            kamar_dihapus = data[hotel].pop(indeks)
            simpan_data_kamar(data)
            print(f"\n[Sukses] Kamar '{kamar_dihapus['nama']}' berhasil dihapus!")
        else:
            print("\n[!] Nomor kamar tidak valid.")
    except ValueError:
        print("\n[!] Harap masukkan angka yang valid.")
    except KeyboardInterrupt:
        print("\n[!] Jangan menekan CTRL + C!")


def lihatreservasi():
    print("\n" + "=" * 60)
    print("            DATA RESERVASI CUSTOMER")
    print("=" * 60)

    try:
        with open(FILE_RESERVASI, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[Info] Belum ada data reservasi atau file tidak ditemukan.")
        return

    if not data:
        print("[Info] Belum ada reservasi.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama Customer", "Hotel", "Kamar", "Tipe"]
    table.align["Nama Customer"] = "l"
    table.align["Hotel"] = "l"
    table.align["Kamar"] = "l"
    table.align["Tipe"] = "l"

    for idx, i in enumerate(data, start=1):
        nama_hotel = i.get("hotel", "Tidak Diketahui")
        table.add_row(
            [
                idx,
                i.get("nama", "-"),
                nama_hotel,
                i.get("kamar", "-"),
                i.get("tipe", "-"),
            ]
        )

    print(table)


def lihat_kamar_tersedia(hotel):
    data = muat_data_kamar()

    print("\n" + "=" * 55)
    print(f"       DAFTAR KAMAR TERSEDIA DI HOTEL {hotel.upper()}       ")
    print("=" * 55)

    kamar_tersedia = [
        k for k in data[hotel] if k.get("status", "").lower() == "tersedia"
    ]

    if not kamar_tersedia:
        print(
            f"[Info] Mohon maaf, saat ini belum ada kamar yang tersedia di Hotel {hotel}."
        )
        return

    table = PrettyTable()
    table.field_names = [
        "No",
        "Nama Kamar",
        "Tipe Kamar",
        "Harga",
    ]
    table.align["Nama Kamar"] = "l"
    table.align["Tipe Kamar"] = "l"
    table.align["Harga"] = "r"

    for index, kamar in enumerate(kamar_tersedia, start=1):
        harga_str = f"Rp {kamar['harga']:,}"
        table.add_row(
            [index, kamar["nama"], kamar["tipe"], harga_str]
        )

    print(table)


def pesan_kamar(username_login, hotel):
    """Memesan kamar, memotong saldo akun, dan meminta top up jika saldo kurang."""
    print(f"\n=== PEMESANAN KAMAR HOTEL {hotel.upper()} ===")

    akun = muat_data_akun()
    data_kamar = muat_data_kamar()

    user_data = akun["user"].get(username_login, {})
    if isinstance(user_data, str):
        saldo_user = 0
    else:
        saldo_user = user_data.get("saldo", 0)

    print(f"Saldo Anda saat ini: {format_rupiah(saldo_user)}")

    kamar_tersedia = [
        k for k in data_kamar[hotel] if k.get("status", "").lower() == "tersedia"
    ]

    if not kamar_tersedia:
        print(
            f"[Info] Tidak ada kamar yang tersedia di Hotel {hotel} untuk dipesan."
        )
        return

    print(f"\n--- DAFTAR KAMAR TERSEDIA DI {hotel.upper()} ---")
    table = PrettyTable()
    table.field_names = ["No", "Nama Kamar", "Tipe Kamar", "Harga"]
    table.align["Nama Kamar"] = "l"
    table.align["Tipe Kamar"] = "l"
    table.align["Harga"] = "r"

    for idx, k in enumerate(kamar_tersedia, start=1):
        harga_str = f"Rp {k['harga']:,}"
        table.add_row([idx, k["nama"], k["tipe"], harga_str])

    print(table)

    try:
        pilihan = int(
            input("Masukkan NOMOR kamar yang ingin dipesan (0 untuk batal): ")
        )
        if pilihan == 0:
            return

        indeks = pilihan - 1
        if 0 <= indeks < len(kamar_tersedia):
            kamar_dipilih = kamar_tersedia[indeks]
            harga_kamar = kamar_dipilih["harga"]

            while saldo_user < harga_kamar:
                print(f"\n[!] Saldo Anda tidak cukup!")
                print(f" Harga Kamar : {format_rupiah(harga_kamar)}")
                print(f" Saldo Anda  : {format_rupiah(saldo_user)}")
                print(f" Kekurangan  : {format_rupiah(harga_kamar - saldo_user)}")

                opsi = (
                    input("Apakah Anda ingin melakukan Top Up sekarang? (y/t): ")
                    .strip()
                    .lower()
                )
                if opsi == "y":
                    saldo_user = topup_saldo(username_login)
                else:
                    print(
                        "[Info] Pemesanan dibatalkan karena saldo tidak mencukupi."
                    )
                    return

            while True:
                konfirmasi = (
                    input(
                        f"Yakin ingin memesan kamar {kamar_dipilih['nama']} ({kamar_dipilih['tipe']}) seharga {format_rupiah(harga_kamar)}? (y/t): "
                    )
                    .strip()
                    .lower()
                )
                if konfirmasi in ["y", "t"]:
                    break
                print("[!] Masukkan pilihan yang valid ('y' atau 't').")

            if konfirmasi != "y":
                print("[Info] Pemesanan dibatalkan.")
                return

            if isinstance(akun["user"][username_login], str):
                akun["user"][username_login] = {
                    "password": akun["user"][username_login],
                    "saldo": saldo_user - harga_kamar,
                }
            else:
                akun["user"][username_login]["saldo"] = (
                    saldo_user - harga_kamar
                )
            simpan_data_akun(akun)

            data_baru_reservasi = {
                "username": username_login,
                "nama": username_login,
                "hotel": hotel,
                "kamar": kamar_dipilih["nama"],
                "tipe": kamar_dipilih["tipe"],
                "harga": harga_kamar,
            }

            try:
                with open(FILE_RESERVASI, "r", encoding="utf-8") as f:
                    data_reservasi = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data_reservasi = []

            data_reservasi.append(data_baru_reservasi)

            with open(FILE_RESERVASI, "w", encoding="utf-8") as f:
                json.dump(data_reservasi, f, indent=4, ensure_ascii=False)

            for k in data_kamar[hotel]:
                if k["nama"] == kamar_dipilih["nama"]:
                    k["status"] = "Tidak Tersedia"
                    break

            simpan_data_kamar(data_kamar)

            sisa_saldo_terkini = (
                akun["user"][username_login]["saldo"]
                if isinstance(akun["user"][username_login], dict)
                else 0
            )
            print(
                f"\n[Sukses] Kamar {kamar_dipilih['nama']} di Hotel {hotel} berhasil dipesan!"
            )
            print(f"Sisa Saldo Anda: {format_rupiah(sisa_saldo_terkini)}")
        else:
            print("[!] Nomor kamar tidak valid.")
    except ValueError:
        print("[!] Harap masukkan angka yang valid.")
    except KeyboardInterrupt:
        print("\n[!] Jangan menekan CTRL + C!")


def lihat_reservasi_sendiri(username_login):
    print("\n" + "=" * 60)
    print(
        f"            RIWAYAT RESERVASI ATAS NAMA: {username_login}            "
    )
    print("=" * 60)

    try:
        with open(FILE_RESERVASI, "r", encoding="utf-8") as f:
            data_reservasi = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[Info] Belum ada data reservasi.")
        return

    reservasi_user = [
        r for r in data_reservasi if r.get("username") == username_login
    ]

    if not reservasi_user:
        print("[Info] Anda belum memiliki riwayat reservasi kamar.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Hotel", "Nama Kamar", "Tipe Kamar", "Harga"]
    table.align["Hotel"] = "l"
    table.align["Nama Kamar"] = "l"
    table.align["Tipe Kamar"] = "l"
    table.align["Harga"] = "r"

    for idx, r in enumerate(reservasi_user, start=1):
        harga_str = f"Rp {r.get('harga', 0):,}"
        table.add_row(
            [
                idx,
                r.get("hotel", "-"),
                r.get("kamar", "-"),
                r.get("tipe", "-"),
                harga_str,
            ]
        )

    print(table)


def batalkan_reservasi(username_login):
    print("\n=== BATALKAN RESERVASI KAMAR ===")

    try:
        with open(FILE_RESERVASI, "r", encoding="utf-8") as f:
            data_reservasi = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[Info] Belum ada data reservasi.")
        return

    reservasi_user = [
        r for r in data_reservasi if r.get("username") == username_login
    ]

    if not reservasi_user:
        print("[Info] Anda tidak memiliki reservasi untuk dibatalkan.")
        return

    print("Daftar Reservasi Anda:")
    table = PrettyTable()
    table.field_names = ["No", "Hotel", "Nama Kamar", "Tipe Kamar"]
    table.align["Hotel"] = "l"
    table.align["Nama Kamar"] = "l"
    table.align["Tipe Kamar"] = "l"

    for idx, r in enumerate(reservasi_user, start=1):
        table.add_row(
            [idx, r.get("hotel", "-"), r.get("kamar", "-"), r.get("tipe", "-")]
        )

    print(table)

    try:
        pilihan = int(
            input(
                "Masukkan NOMOR reservasi yang ingin dibatalkan (0 untuk batal): "
            )
        )
        if pilihan == 0:
            return

        indeks = pilihan - 1
        if 0 <= indeks < len(reservasi_user):
            target_batal = reservasi_user[indeks]

            while True:
                konfirmasi = (
                    input(
                        f"Yakin ingin membatalkan reservasi kamar {target_batal['kamar']} di {target_batal['hotel']}? (y/t): "
                    )
                    .strip()
                    .lower()
                )
                if konfirmasi in ["y", "t"]:
                    break
                print("[!] Masukkan pilihan yang valid ('y' atau 't').")

            if konfirmasi != "y":
                print("[Info] Pembatalan dibatalkan.")
                return

            data_reservasi.remove(target_batal)
            with open(FILE_RESERVASI, "w", encoding="utf-8") as f:
                json.dump(data_reservasi, f, indent=4, ensure_ascii=False)

            data_kamar = muat_data_kamar()
            hotel_target = target_batal["hotel"]
            nama_kamar_target = target_batal["kamar"]

            if hotel_target in data_kamar:
                for k in data_kamar[hotel_target]:
                    if k["nama"] == nama_kamar_target:
                        k["status"] = "Tersedia"
                        break
                simpan_data_kamar(data_kamar)

            print(
                f"\n[Sukses] Reservasi kamar {nama_kamar_target} berhasil dibatalkan!"
            )
        else:
            print("[!] Nomor reservasi tidak valid.")
    except ValueError:
        print("[!] Harap masukkan angka yang valid.")
    except KeyboardInterrupt:
        print("\n[!] Jangan menekan CTRL + C!")


def cetak_invoice(username_login):
    print("\n" + "=" * 60)
    print("                CETAK INVOICE / STRUK PEMBAYARAN")
    print("=" * 60)

    try:
        with open(FILE_RESERVASI, "r", encoding="utf-8") as f:
            data_reservasi = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[Info] Belum ada data reservasi.")
        return

    reservasi_user = [
        r for r in data_reservasi if r.get("username") == username_login
    ]

    if not reservasi_user:
        print("[Info] Anda belum memiliki reservasi untuk dicetak invoicenya.")
        time.sleep(1.5)
        return

    print("Pilih reservasi yang ingin dicetak invoicenya:")
    table = PrettyTable()
    table.field_names = ["No", "Hotel", "Nama Kamar", "Tipe", "Harga"]
    table.align["Hotel"] = "l"
    table.align["Nama Kamar"] = "l"
    table.align["Tipe"] = "l"
    table.align["Harga"] = "r"

    for idx, r in enumerate(reservasi_user, start=1):
        harga_str = f"Rp {r.get('harga', 0):,}"
        table.add_row(
            [
                idx,
                r.get("hotel", "-"),
                r.get("kamar", "-"),
                r.get("tipe", "-"),
                harga_str,
            ]
        )

    print(table)

    try:
        pilihan = int(input("Masukkan NOMOR reservasi (0 untuk batal): "))
        if pilihan == 0:
            return

        indeks = pilihan - 1
        if 0 <= indeks < len(reservasi_user):
            inv = reservasi_user[indeks]

            harga_sewa = inv.get("harga", 0)
            pajak_daerah = int(harga_sewa * 0.10)
            total_tagihan = harga_sewa + pajak_daerah

            waktu_cetak = time.strftime("%d-%m-%Y %H:%M:%S")

            print("\n[Sedang mencetak invoice...]")
            time.sleep(1.5)

            print("\n" + "=" * 65)
            print("                 APLIKASI HOTEL SAMARINDA")
            print("         Jl. Jenderal Sudirman No. 88, Samarinda, Kaltim")
            print("=" * 65)
            print(" [ IDENTITAS TAMU ]")
            print(f" Username      : {inv.get('username', '-')}")
            print(f" Nama Tamu     : {inv.get('nama', '-')}")
            print("-" * 65)
            print(" [ INFORMASI MENGINAP ]")
            print(f" Hotel Tujuan  : Hotel {inv.get('hotel', '-')}")
            print(f" Kamar         : {inv.get('kamar', '-')}")
            print(f" Tipe Kamar    : {inv.get('tipe', '-')}")
            print("-" * 65)
            print(" [ RINCIAN BIAYA ]")
            print(f" • Biaya Sewa Kamar      : Rp {harga_sewa:,}")
            print(f" • Pajak Daerah (10%)    : Rp {pajak_daerah:,}")
            print("-----------------------------------------------------------------")
            print(f" TOTAL TAGIHAN           : Rp {total_tagihan:,}")
            print("=" * 65)
            print(" [ METODE & KETENTUAN PEMBAYARAN ]")
            print(" 1. Pembayaran dapat dilakukan via Transfer Bank (BCA/BRI/Mandiri)")
            print("  atau QRIS pada saat Check-In di resepsionis.")
            print(" 2. Harap membawa bukti reservasi/invoice ini saat kedatangan.")
            print(" 3. Pembatalan gratis maksimal 1 hari sebelum jadwal menginap.")
            print("=" * 65)

        else:
            print("[!] Nomor reservasi tidak valid.")
            time.sleep(1.5)
    except ValueError:
        print("[!] Harap masukkan angka yang valid.")
        time.sleep(1.5)
    except KeyboardInterrupt: 
        print("\n[!] Jangan menekan CTRL + C!")


def user_menu(username_login):
    """Menu Utama khusus User."""
    hotel = pilih_hotel()

    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("\n" + "=" * 35)
        print(f"    MENU USER ({username_login}) - Hotel {hotel}")
        print("=" * 35)
        print("1. Lihat Data Kamar")
        print("2. Pesan Kamar")
        print("3. Lihat Reservasi")
        print("4. Batalkan Reservasi")
        print("5. Cetak Invoice")
        print("6. Topup")
        print("7. Ganti Hotel")
        print("0. Logout")

        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                lihat_kamar_tersedia(hotel)
            elif pilihan == 2:
                pesan_kamar(username_login, hotel)
            elif pilihan == 3:
                lihat_reservasi_sendiri(username_login)
            elif pilihan == 4:
                batalkan_reservasi(username_login)
            elif pilihan == 5:
                cetak_invoice(username_login)
            elif pilihan == 6:
                topup_saldo(username_login)
            elif pilihan == 7:
                hotel = pilih_hotel()
            elif pilihan == 0:
                print("\nKeluar dari menu user...")
                break
            else:
                print("[!] Pilihan tidak valid.")
        except ValueError:
            print("[!] INPUT HARUS BERUPA ANGKA")
        except KeyboardInterrupt:
            print("\n[!] Jangan menekan CTRL + C!")


def admin():
    hotel = pilih_hotel()
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("\n" + "=" * 30)
        print(f"    MENU ADMIN - Hotel {hotel}")
        print("=" * 30)
        print("1. Tambah Kamar Baru")
        print("2. Lihat Semua Kamar")
        print("3. Lihat Daftar Reservasi (Semua Hotel)")
        print("4. Ubah Harga dan Status Kamar")
        print("5. Hapus Data Kamar")
        print("6. Ganti Pilihan Hotel")
        print("0. Logout")

        try:
            pilihan = int(input("Pilih menu : "))
            if pilihan == 1:
                tambah_tipe_kamar(hotel)
            elif pilihan == 2:
                tampilkan_kamar(hotel)
            elif pilihan == 3:
                lihatreservasi()
            elif pilihan == 4:
                ubah_kamar(hotel)
            elif pilihan == 5:
                hapus_kamar(hotel)
            elif pilihan == 6:
                hotel = pilih_hotel()
            elif pilihan == 0:
                print("\nKeluar dari menu admin...")
                break
            else:
                print("[!] Pilihan tidak valid.")
        except ValueError:
            print("[!] INPUT HARUS BERUPA ANGKA")
        except KeyboardInterrupt:
            print("\n[!] Jangan menekan CTRL + C!")


def menu_awal():
    while True:
        try:
            print("\n" + "=" * 40)
            print("    SISTEM RESERVASI HOTEL MULTI")
            print("=" * 40)
            print("1. Login")
            print("2. Registrasi Akun")
            print("0. Keluar Aplikasi")

            pilihan = input("Pilih menu: ").strip()

            os.system("cls" if os.name == "nt" else "clear")
            if pilihan == "1":
                role, username = login()
                if role == "admin":
                    admin()
                elif role == "user":
                    user_menu(username)
            elif pilihan == "2":
                registrasi()
            elif pilihan == "0":
                print("\nTERIMA KASIH TELAH MENGGUNAKAN APLIKASI INI.")
                break
            else:
                print("[!] Pilihan tidak valid.")

        except KeyboardInterrupt:
            print("\n[!] Jangan menekan CTRL + C!")

menu_awal()