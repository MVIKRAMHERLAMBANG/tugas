class Karyawan:
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan

    def hitung_gaji(self):
        # Metode placeholder yang akan di-override oleh subclass
        return 0

    def tampilkan_info(self):
        print(f"ID: {self.id_karyawan} | Nama: {self.nama}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        # Penggunaan super() untuk memanggil konstruktor kelas induk
        super().__init__(nama, id_karyawan)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, upah_harian, hari_kerja):
        # Penggunaan super() untuk inisialisasi atribut nama dan ID
        super().__init__(nama, id_karyawan)
        self.upah_harian = upah_harian
        self.hari_kerja = hari_kerja

    def hitung_gaji(self):
        return self.upah_harian * self.hari_kerja

# Demonstrasi Subtyping
def cetak_slip_gaji(karyawan: Karyawan):
    karyawan.tampilkan_info()
    print(f"Total Gaji: Rp{karyawan.hitung_gaji()}\n")

# Contoh Penggunaan
karyawan1 = KaryawanTetap("Vikram", "STF-001", 5000000, 1000000)
karyawan2 = KaryawanKontrak("Andi", "CON-002", 150000, 20)

cetak_slip_gaji(karyawan1)
cetak_slip_gaji(karyawan2)