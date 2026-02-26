class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = "Tersedia"

    def tampilkan_info(self):
        print("Judul :", self.judul)
        print("Penulis :", self.penulis)
        print("Tahun :", self.tahun)
        print("Status :", self.status)

    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            print("Buku berhasil dipinjam")
        else:
            print("Buku sedang dipinjam")

    def kembalikan(self):
        self.status = "Tersedia"
        print("Buku berhasil dikembalikan")


class Anggota:
    def __init__(self, nama):
        # State / Atribut
        self.nama = nama

    # Behavior / Method
    def pinjam_buku(self, buku):
        print(self.nama, "meminjam buku")
        buku.pinjam()

    def kembalikan_buku(self, buku):
        print(self.nama, "mengembalikan buku")
        buku.kembalikan()

    def tampilkan_info(self):
        print("Nama Anggota :", self.nama)


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.daftar_anggota = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' ditambahkan ke perpustakaan {self.nama}.")

    def hapus_buku(self, buku):
        self.daftar_buku.remove(buku)

    def daftar_semua_buku(self):
        print(f"\nDaftar semua buku di {self.nama}:")
        for buku in self.daftar_buku:
            buku.tampilkan_info() # Corrected method name
            print("------------------")


# Objek Buku
buku1 = Buku("Python Dasar", "Sapri", 2022)
buku2 = Buku("Algoritma", "Toy", 2021)
buku3 = Buku("OOP Python", "Rinz", 2023)

# Objek Anggota
anggota1 = Anggota("Ali")
anggota2 = Anggota("Mbut")
anggota3 = Anggota("Andi")

# Objek Perpustakaan - Initialize here
perpustakaan = Perpustakaan("Perpustakaan Kampus")

# Menambahkan buku ke perpustakaan
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tambah_buku(buku3)


print("----DAFTAR BUKU----")
buku1.tampilkan_info()
print("------------------")
buku2.tampilkan_info()
print("------------------")
buku3.tampilkan_info()
print("------------------")

print(       )

print("DAFTAR ANGGOTA")
anggota1.tampilkan_info()
anggota2.tampilkan_info()
anggota3.tampilkan_info()


print(       )

print("----PEMINJAMAN BUKU----")
anggota1.pinjam_buku(buku3)

buku3.tampilkan_info()
print("------------------")

anggota3.kembalikan_buku(buku2)

buku2.tampilkan_info()

print(       )
print("----DAFTAR BUKU DI PERPUSTAKAAN----")
perpustakaan.daftar_semua_buku()
