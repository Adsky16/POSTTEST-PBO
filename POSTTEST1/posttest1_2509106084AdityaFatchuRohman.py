class Produk:

    nama_toko = "Toko Kaca & Aluminium sahabat"
    jumlah_produk = 0
    jenis_toko = "Toko Kaca & Aluminium"

    def __init__(self, nama, jenis, stok, harga):
        self.nama = nama
        self.jenis = jenis
        self.__stok = stok
        self.__harga = harga

        Produk.jumlah_produk += 1
        
    def tampilkan_info(self):
        print(f"Nama Produk: {self.nama}")
        print(f"Jenis      : {self.jenis}")
        print(f"Stok       : {self.stok}")
        print(f"Harga      : Rp {self.harga}")

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.stok += jumlah
            print(f"Stok produk {self.nama} berhasil ditambahkan sebanyak {jumlah}.")
        else:
            print("Jumlah stok yang ditambahkan harus lebih dari 0.")

    def kurangi_stok(self, jumlah):
        if jumlah > 0:
            if jumlah <= self.stok:
                self.stok -= jumlah
                print(f"Stok produk {self.nama} berhasil dikurangi sebanyak {jumlah}.")
            else:
                print(f"Stok produk {self.nama} tidak mencukupi. Stok saat ini: {self.stok}.")
        else:
            print("Jumlah stok yang dikurangi harus lebih dari 0.")

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai):
        if nilai >= 0:
            self.__stok = nilai
        else:
            print("Stok tidak boleh negatif.")

    @property
    def harga(self):
        return self.__harga
    
    @harga.setter
    def harga(self, nilai):
        if nilai > 0:
            self.__harga = nilai
        else:
            print("Harga harus lebih dari 0.")

    @classmethod
    def info_toko(cls):
        print(f"Nama Toko    : {cls.nama_toko}")
        print(f"Jenis Toko   : {cls.jenis_toko}")
        print(f"Jumlah Produk: {cls.jumlah_produk}")

    @staticmethod
    def cek_kebutuhan_stok(stok, jumlah):
        if jumlah <= stok:
            print("Stok mencukupi.")
            return True
        else:
            print("Stok tidak mencukupi.")
            return False

class Pelanggan:
    tipe_pelanggan = "Perorangan"
    jumlah_pelanggan = 0
    status_pelanggan = "Aktif"

    def __init__(self, nama, nomor_hp, alamat):
        self.nama = nama
        self.__nomor_hp = nomor_hp
        self.alamat = alamat

        Pelanggan.jumlah_pelanggan += 1

    def tampilkan_data(self):
        print(f"Nama Pelanggan : {self.nama}")
        print(f"Nomor HP       : {self.nomor_hp}")
        print(f"Alamat         : {self.alamat}")

    def ubah_nomor_hp(self, nomor_baru):
        self.nomor_hp = nomor_baru
    
    def ubah_alamat(self, alamat_baru):
        self.alamat = alamat_baru
        print("Alamat berhasil diubah.")

    @property
    def nomor_hp(self):
        return self.__nomor_hp

    @nomor_hp.setter
    def nomor_hp(self, nilai):
        if len(nilai) >= 11:
            self.__nomor_hp = nilai
            print("Nomor HP berhasil diubah.")
            return True
        else:
            print("Nomor HP harus memiliki minimal 11 digit.")
            return False

    @classmethod
    def info_pelanggan(cls):
        print(f"Tipe Pelanggan  : {cls.tipe_pelanggan}")
        print(f"Jumlah Pelanggan: {cls.jumlah_pelanggan}")
        print(f"Status Pelanggan: {cls.status_pelanggan}")

    @staticmethod
    def format_nomor_hp(nomor_hp):
        if len(nomor_hp) >= 11:
            return f"{nomor_hp[:4]}-{nomor_hp[4:8]}-{nomor_hp[8:]}"
        else:
            return "Nomor HP tidak valid."

class Transaksi:
    jumlah_transaksi = 0
    status_transaksi = "Berhasil"
    nama_toko = "Toko Kaca & Aluminium sahabat"

    def __init__(self, pelanggan, produk, jumlah_beli):
        self.pelanggan = pelanggan
        self.produk = produk
        self.__jumlah_beli = jumlah_beli
        self.__total_harga = 0
        Transaksi.jumlah_transaksi += 1

    def hitung_total(self):
        if self.jumlah_beli > 0:
            self.__total_harga = self.produk.harga * self.jumlah_beli
            return self.__total_harga
        else:
            self.__total_harga = 0
            return 0

    def proses_pembelian(self):
        if self.jumlah_beli <= 0:
            print("Jumlah pembelian harus lebih dari 0.")
            return

        if self.jumlah_beli <= self.produk.stok:
            self.produk.kurangi_stok(self.jumlah_beli)
            self.hitung_total()
            print("Pembelian berhasil diproses.")
        else:
            print("Pembelian gagal. Stok produk tidak mencukupi.")

    def tampilkan_transaksi(self):
        print("===== DETAIL TRANSAKSI =====")
        print(f"Nama Pelanggan : {self.pelanggan.nama}")
        print(f"Produk         : {self.produk.nama}")
        print(f"Jumlah Beli    : {self.jumlah_beli}")
        print(f"Harga Satuan   : Rp {self.produk.harga}")
        print(f"Total Harga    : Rp {self.total_harga}")
        print(f"Status         : {Transaksi.status_transaksi}")

    def cetak_struk(self):
        print("\n========== STRUK ==========")
        print(f"Toko           : {Transaksi.nama_toko}")
        print(f"Pelanggan      : {self.pelanggan.nama}")
        print(f"Produk         : {self.produk.nama}")
        print(f"Jumlah         : {self.jumlah_beli}")
        print(f"Harga Satuan   : Rp {self.produk.harga}")
        print(f"Total Bayar    : Rp {self.total_harga}")
        print("===========================")
        print("Terima kasih telah berbelanja.")

    @property
    def jumlah_beli(self):
        return self.__jumlah_beli

    @jumlah_beli.setter
    def jumlah_beli(self, nilai):
        if nilai > 0:
            self.__jumlah_beli = nilai
        else:
            print("Jumlah pembelian harus lebih dari 0.")

    @property
    def total_harga(self):
        return self.__total_harga

    @classmethod
    def info_transaksi(cls):
        print(f"Nama Toko         : {cls.nama_toko}")
        print(f"Jumlah Transaksi  : {cls.jumlah_transaksi}")
        print(f"Status Transaksi  : {cls.status_transaksi}")

    @staticmethod
    def format_rupiah(nilai):
        return f"Rp {nilai:,}".replace(",", ".")

produk1 = Produk("Kaca Tempered", "Kaca", 50, 150000)
produk2 = Produk("Aluminium Frame", "Aluminium", 30, 200000)

pelanggan1 = Pelanggan("Aditya", "08123456789", "Samarinda")
pelanggan2 = Pelanggan("Budi", "08234567890", "Samarinda")

transaksi1 = Transaksi(pelanggan1, produk1, 3)
transaksi2 = Transaksi(pelanggan2, produk2, 5)

print("\n===== PENGUJIAN PRODUK =====")

produk1.tampilkan_info()
produk1.tambah_stok(10)
produk1.kurangi_stok(5)

produk2.tampilkan_info()
produk2.tambah_stok(20)
produk2.kurangi_stok(10)

print("\n===== CEK KEBUTUHAN STOK =====")

Produk.cek_kebutuhan_stok(produk1.stok, 30)
Produk.cek_kebutuhan_stok(produk2.stok, 100)

print("\n===== INFO TOKO =====")

Produk.info_toko()

print("\n===== PENGUJIAN PELANGGAN =====")

pelanggan1.tampilkan_data()
pelanggan1.ubah_nomor_hp("08111111111")
pelanggan1.ubah_alamat("Balikpapan")

pelanggan2.tampilkan_data()
pelanggan2.ubah_nomor_hp("08222222222")
pelanggan2.ubah_alamat("Samarinda")

print("\n===== FORMAT NOMOR HP =====")

print(Pelanggan.format_nomor_hp(pelanggan1.nomor_hp))
print(Pelanggan.format_nomor_hp(pelanggan2.nomor_hp))

Pelanggan.info_pelanggan()

print("\n===== PENGUJIAN TRANSAKSI 1 =====")

print("Total transaksi 1:")
print(f"Rp {transaksi1.hitung_total()}")

print("\nProses transaksi 1:")
transaksi1.proses_pembelian()

print("\nDetail transaksi 1:")
transaksi1.tampilkan_transaksi()

print("\nStruk transaksi 1:")
transaksi1.cetak_struk()

print("\n===== TRANSAKSI 2 =====")

print(f"Total transaksi 2: Rp {transaksi2.hitung_total()}")

transaksi2.proses_pembelian()
transaksi2.tampilkan_transaksi()
transaksi2.cetak_struk()

print("\n===== INFO TRANSAKSI =====")

Transaksi.info_transaksi()

print("\n===== FORMAT RUPIAH =====")

print(Transaksi.format_rupiah(150000))
print(Transaksi.format_rupiah(450000))

print("\n===== TEST SETTER STOK =====")

produk1.stok = 100
print(f"Stok baru produk 1: {produk1.stok}")

produk1.stok = -10

produk1.harga = 175000
print(f"Harga baru produk 1: Rp {produk1.harga}")

produk1.harga = 0

pelanggan1.nomor_hp = "08133333333"
print(f"Nomor HP baru: {pelanggan1.nomor_hp}")

pelanggan1.nomor_hp = "12345"

transaksi1.jumlah_beli = 5
print(f"Jumlah beli baru: {transaksi1.jumlah_beli}")

transaksi1.jumlah_beli = 0
