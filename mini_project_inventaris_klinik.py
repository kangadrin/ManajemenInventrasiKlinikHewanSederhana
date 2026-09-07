# ============================================================
#  MINI PROJECT 2 : SISTEM MANAJEMEN INVENTARIS KLINIK
#                   DAN OBAT-OBATAN
#  Materi : Python Basic (Bootcamp Data Science)
#  ------------------------------------------------------------
#  Nama  : (isi nama kamu)
#  Kelas : (isi kelas kamu)
#  ------------------------------------------------------------
#  Program ini dibuat HANYA dari materi Python Basic :
#  - Materi 2 : variabel & tipe data, operator, input-output,
#               string formatting, logika if-else
#  - Materi 3 : list, dictionary, tuple, set, function def,
#               function lambda, built-in function
#  - Materi 4 : try-except, for / while / break,
#               list comprehension, mini program
#  Cocok dijalankan di Google Colab maupun terminal.
# ============================================================

# ===== 1. DATA AWAL BARANG (LIST & DICTIONARY) =====

# List berisi beberapa dictionary (Materi 3)
# Tanggal kedaluwarsa ditulis dengan format YYYY-MM
daftar_obat = [
    {"kode": "OB001", "nama": "Paracetamol", "golongan": "Analgesik",
     "stok": 50, "harga": 15000, "expired": "2027-08"},
    {"kode": "OB002", "nama": "Amoxicillin", "golongan": "Antibiotik",
     "stok": 4, "harga": 45000, "expired": "2026-11"},
    {"kode": "OB003", "nama": "Vitamin C", "golongan": "Vitamin",
     "stok": 0, "harga": 12000, "expired": "2026-03"},
    {"kode": "OB004", "nama": "Antasida", "golongan": "Lambung",
     "stok": 25, "harga": 18000, "expired": "2027-01"},
    {"kode": "OB005", "nama": "Salep Kulit", "golongan": "Dermatologi",
     "stok": 3, "harga": 28000, "expired": "2026-06"},
]

# Daftar pengguna (petugas) yang memakai program ini
daftar_pengguna = ["Andi", "Siti"]

# Riwayat transaksi : list berisi tuple
# isi tuple : (nomor, nama_pengguna, nama_barang, jumlah, total)
riwayat_transaksi = []
nomor_transaksi = 1

# ===== 2. FUNCTION & PROCEDURE =====

def tampilkan_obat():
    # Procedure : function yang tidak mengembalikan nilai (Materi 3)
    print("=" * 64)
    print("DAFTAR BARANG KLINIK")
    print("=" * 64)
    for i in range(len(daftar_obat)):
        o = daftar_obat[i]
        print(o["kode"] + " | " + o["nama"] + " | " + o["golongan"] +
              " | stok " + str(o["stok"]) + " | Rp " + str(o["harga"]) +
              " | exp " + o["expired"])
    print("=" * 64)
    print("Jumlah jenis barang :", len(daftar_obat))   # built-in len()

def cari_barang(kode):
    # List comprehension : ambil barang yang kodenya cocok (Materi 4)
    hasil = [o for o in daftar_obat if o["kode"] == kode]
    return hasil

def cari_per_golongan(golongan):
    # List comprehension : filter barang berdasarkan golongan
    hasil = [o for o in daftar_obat if o["golongan"] == golongan]
    return hasil

def tambah_barang(kode, nama, golongan, stok, harga, expired):
    # Menambahkan satu dictionary baru ke dalam list (mutable)
    barang_baru = {"kode": kode, "nama": nama, "golongan": golongan,
                   "stok": stok, "harga": harga, "expired": expired}
    daftar_obat.append(barang_baru)
    print("Barang", nama, "berhasil ditambahkan.")

def hapus_barang(kode):
    # Hapus barang : buat list baru tanpa barang tsb (list comprehension)
    global daftar_obat
    daftar_baru = [o for o in daftar_obat if o["kode"] != kode]
    if len(daftar_baru) == len(daftar_obat):
        print("Barang dengan kode", kode, "tidak ditemukan.")
    else:
        daftar_obat = daftar_baru
        print("Barang dengan kode", kode, "berhasil dihapus.")

def restok_barang(kode, jumlah):
    # Update stok : menambah stok barang yang sudah ada
    for i in range(len(daftar_obat)):
        if daftar_obat[i]["kode"] == kode:
            daftar_obat[i]["stok"] = daftar_obat[i]["stok"] + jumlah
            print("Stok", daftar_obat[i]["nama"], "bertambah", jumlah,
                  "pcs. Stok sekarang :", daftar_obat[i]["stok"])
            return
    print("Barang dengan kode", kode, "tidak ditemukan.")

def jual_barang(kode, jumlah, nama_pengguna):
    # Penjualan : stok berkurang & transaksi dicatat ke riwayat
    global nomor_transaksi
    for i in range(len(daftar_obat)):
        if daftar_obat[i]["kode"] == kode:
            if daftar_obat[i]["stok"] >= jumlah:
                daftar_obat[i]["stok"] = daftar_obat[i]["stok"] - jumlah
                total = daftar_obat[i]["harga"] * jumlah
                riwayat_transaksi.append((nomor_transaksi, nama_pengguna,
                                          daftar_obat[i]["nama"],
                                          jumlah, total))
                nomor_transaksi = nomor_transaksi + 1
                print("Penjualan", jumlah, "pcs", daftar_obat[i]["nama"],
                      "oleh", nama_pengguna, "berhasil. Sisa stok :",
                      daftar_obat[i]["stok"])
            else:
                print("Stok tidak mencukupi. Stok tersedia :",
                      daftar_obat[i]["stok"])
            return
    print("Barang dengan kode", kode, "tidak ditemukan.")

# ===== 3. LAPORAN (BUILT-IN & LIST COMPREHENSION) =====

def peringatan_stok():
    # Peringatan : stok habis (0) dan hampir habis (<= 5)
    habis = [o for o in daftar_obat if o["stok"] == 0]
    menipis = [o for o in daftar_obat if 0 < o["stok"] <= 5]
    print("-- STOK HABIS (0 pcs) --")
    if len(habis) == 0:
        print("Tidak ada barang yang stoknya habis.")
    for i in range(len(habis)):
        print(habis[i]["kode"], habis[i]["nama"], "stok 0 pcs")
    print("-- HAMPIR HABIS (<= 5 pcs) --")
    if len(menipis) == 0:
        print("Tidak ada barang yang hampir habis.")
    for i in range(len(menipis)):
        print(menipis[i]["kode"], menipis[i]["nama"],
              "tinggal", menipis[i]["stok"], "pcs.")

def cek_kedaluwarsa(batas="2026-12"):
    # Argumen default (Materi 3) : batas otomatis 2026-12
    # Format tanggal YYYY-MM membuat perbandingan string bisa dipakai
    hasil = [o for o in daftar_obat if o["expired"] < batas]
    if len(hasil) == 0:
        print("Tidak ada barang yang kedaluwarsa sebelum", batas)
    for i in range(len(hasil)):
        print(hasil[i]["kode"], hasil[i]["nama"],
              "expired", hasil[i]["expired"])

def laporan_inventaris():
    # Gabungan built-in function : len, sum, min, max, set
    print("=" * 52)
    print("LAPORAN INVENTARIS KLINIK")
    print("=" * 52)
    total_stok = sum([o["stok"] for o in daftar_obat])
    total_nilai = sum([o["harga"] * o["stok"] for o in daftar_obat])
    print("Jumlah jenis barang :", len(daftar_obat))
    print("Total stok (pcs) :", total_stok)
    print("Total nilai inventaris : Rp", total_nilai)
    print("-" * 52)
    # min & max dengan lambda sebagai kunci pembanding
    print("Barang termahal :",
          max(daftar_obat, key=lambda o: o["harga"])["nama"])
    print("Barang dengan stok terendah :",
          min(daftar_obat, key=lambda o: o["stok"])["nama"])
    print("-" * 52)
    # Set : menghilangkan golongan yang duplikat (Materi 3)
    golongan = set([o["golongan"] for o in daftar_obat])
    print("Golongan yang tersedia :", golongan)
    for g in golongan:
        jumlah = len([o for o in daftar_obat if o["golongan"] == g])
        print("Golongan", g, ":", jumlah, "jenis barang")
    print("-" * 52)
    # Pendapatan dari riwayat transaksi
    pendapatan = sum([t[4] for t in riwayat_transaksi])
    print("Total transaksi :", len(riwayat_transaksi))
    print("Pendapatan penjualan : Rp", pendapatan)

def distribusi_stok(jumlah_cabang):
    # Operator aritmatika : pembagian bulat (//) dan modulo (%)
    total_stok = sum([o["stok"] for o in daftar_obat])
    print("Total stok :", total_stok, "pcs")
    print("Jumlah cabang :", jumlah_cabang)
    print("Setiap cabang menerima :", total_stok // jumlah_cabang, "pcs")
    print("Sisa stok :", total_stok % jumlah_cabang, "pcs")

# ===== 5. MENU UTAMA (WHILE, IF-ELIF-ELSE, TRY-EXCEPT) =====

def menu_utama():
    # while-loop : program berjalan terus sampai pengguna memilih 0
    while True:
        print()
        print("======== MENU INVENTARIS KLINIK ========")
        print(" 1. Lihat semua barang")
        print(" 2. Tambah barang")
        print(" 3. Hapus barang")
        print(" 4. Cari barang (kode / golongan)")
        print(" 5. Update stok (restok)")
        print(" 6. Penjualan barang")
        print(" 7. Peringatan stok (habis / menipis)")
        print(" 8. Obat kedaluwarsa")
        print(" 9. Laporan inventaris")
        print("10. Kelola pengguna & riwayat")
        print("11. Distribusi stok ke cabang (// dan %)")
        print(" 0. Keluar")
        print("========================================")
        pilihan = input("Masukkan pilihan (0-11) : ")

        if pilihan == "1":
            tampilkan_obat()
        elif pilihan == "2":
            # try-except : menangani input yang bukan angka (Materi 4)
            try:
                kode = input("Kode barang : ")
                nama = input("Nama barang : ")
                golongan = input("Golongan : ")
                stok = int(input("Stok : "))
                harga = int(input("Harga : "))
                expired = input("Tanggal kedaluwarsa (YYYY-MM) : ")
                tambah_barang(kode, nama, golongan, stok, harga, expired)
            except ValueError:
                print("Error : stok dan harga harus berupa angka.")
        elif pilihan == "3":
            kode = input("Kode barang yang dihapus : ")
            hapus_barang(kode)
        elif pilihan == "4":
            cara = input("Cari berdasarkan kode (1) atau golongan (2) : ")
            if cara == "1":
                kode = input("Masukkan kode barang : ")
                hasil = cari_barang(kode)
                if len(hasil) == 0:
                    print("Barang dengan kode", kode, "tidak ditemukan.")
                else:
                    o = hasil[0]
                    print(o["nama"], "-", o["golongan"], "- stok",
                          o["stok"], "- Rp", o["harga"], "- exp",
                          o["expired"])
            elif cara == "2":
                golongan = input("Masukkan golongan : ")
                hasil = cari_per_golongan(golongan)
                if len(hasil) == 0:
                    print("Golongan", golongan, "tidak ditemukan.")
                for i in range(len(hasil)):
                    print(hasil[i]["kode"], hasil[i]["nama"],
                          "stok", hasil[i]["stok"])
            else:
                print("Pilihan tidak tersedia.")
        elif pilihan == "5":
            try:
                kode = input("Kode barang : ")
                jumlah = int(input("Jumlah stok ditambah : "))
                restok_barang(kode, jumlah)
            except ValueError:
                print("Error : jumlah harus berupa angka.")
        elif pilihan == "6":
            try:
                kode = input("Kode barang : ")
                jumlah = int(input("Jumlah dijual : "))
                pengguna = input("Nama pengguna (petugas) : ")
                jual_barang(kode, jumlah, pengguna)
            except ValueError:
                print("Error : jumlah harus berupa angka.")
        elif pilihan == "7":
            peringatan_stok()
        elif pilihan == "8":
            batas = input("Batas tanggal (YYYY-MM) : ")
            cek_kedaluwarsa(batas)
        elif pilihan == "9":
            laporan_inventaris()
        elif pilihan == "10":
            # Sub-menu : kelola pengguna & riwayat transaksi
            while True:
                print()
                print("---- KELOLA PENGGUNA ----")
                print("1. Lihat daftar pengguna")
                print("2. Tambah pengguna")
                print("3. Riwayat transaksi")
                print("0. Kembali ke menu utama")
                sub = input("Pilihan : ")
                if sub == "1":
                    print("Daftar pengguna :", daftar_pengguna)
                elif sub == "2":
                    nama_baru = input("Nama pengguna baru : ")
                    daftar_pengguna.append(nama_baru)
                    print("Pengguna", nama_baru, "berhasil ditambahkan.")
                elif sub == "3":
                    if len(riwayat_transaksi) == 0:
                        print("Belum ada transaksi.")
                    for i in range(len(riwayat_transaksi)):
                        t = riwayat_transaksi[i]
                        print("No." + str(t[0]), "|", t[1], "|",
                              t[2], "x", t[3], "| Rp", t[4])
                    print("Total transaksi :", len(riwayat_transaksi))
                elif sub == "0":
                    break   # kembali ke menu utama
                else:
                    print("Pilihan tidak tersedia.")
        elif pilihan == "11":
            # ZeroDivisionError : terjadi jika jumlah_cabang bernilai 0
            try:
                jumlah_cabang = int(input("Jumlah cabang : "))
                distribusi_stok(jumlah_cabang)
            except ZeroDivisionError:
                print("Error : jumlah cabang tidak boleh 0 (nol).")
            except ValueError:
                print("Error : jumlah cabang harus berupa angka.")
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini.")
            break   # menghentikan while-loop (Materi 4)
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")

# Program dimulai dari sini
menu_utama()
