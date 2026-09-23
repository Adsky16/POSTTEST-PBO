Sistem Pengelolaan Pesanan, Produk dan Stok pada Toko Kaca & Aluminium

1. Deskripsi Program

Program ini merupakan aplikasi sederhana berbasis Python yang digunakan untuk mengelola data produk, pelanggan, stok, dan transaksi pada Toko Kaca & Aluminium. Program dibuat menggunakan konsep Pemrograman Berorientasi Objek (PBO/OOP), sehingga data dan fungsi yang berkaitan dikelompokkan ke dalam beberapa class.
Program memiliki tiga class utama, yaitu `Produk`, `Pelanggan`, dan `Transaksi`. Masing-masing class memiliki atribut dan method yang memiliki tugas yang berbeda.

2. Tujuan Program

Program dibuat untuk:
    1. Mengelola data produk seperti nama, jenis, stok, dan harga.
    2. Menambah dan mengurangi stok produk.
    3. Mengecek kebutuhan stok.
    4. Mengelola data pelanggan.
    5. Mengubah nomor HP dan alamat pelanggan.
    6. Membuat dan memproses transaksi pembelian.
    7. Menghitung total harga transaksi.
    8. Menampilkan detail transaksi dan mencetak struk.
    9. Menerapkan konsep dasar PBO seperti object, instance method, class method, static method, dan encapsulation melalui getter/setter.


3. Struktur Class

    3.1 Class `Produk`

        Class `Produk` digunakan untuk menyimpan dan mengelola informasi produk yang tersedia di toko.

        Atribut Class
        - `nama_toko` : menyimpan nama toko.
        - `jumlah_produk` : menghitung jumlah object produk yang dibuat.
        - `jenis_toko` : menyimpan jenis usaha toko.

        Atribut Instance
        - `nama` : nama produk.
        - `jenis` : jenis produk.
        - `__stok` : jumlah stok produk yang bersifat private.
        - `__harga` : harga produk yang bersifat private.

        Instance Method
        - `tampilkan_info()` : menampilkan informasi produk.
        - `tambah_stok(jumlah)` : menambahkan stok produk.
        - `kurangi_stok(jumlah)` : mengurangi stok produk jika stok mencukupi.

        Property dan Setter
        - `stok` : digunakan untuk mengakses dan mengubah stok.
        - `harga` : digunakan untuk mengakses dan mengubah harga.

        Setter melakukan validasi agar:
        - stok tidak boleh bernilai negatif;
        - harga harus lebih dari 0.

        Class Method
        - `info_toko()` : menampilkan informasi umum toko dan jumlah produk.

        Static Method
        - `cek_kebutuhan_stok(stok, jumlah)` : mengecek apakah stok yang tersedia mencukupi kebutuhan suatu pekerjaan atau proyek.

    3.2 Class `Pelanggan`

        Class `Pelanggan` digunakan untuk menyimpan dan mengelola data pelanggan.

        Atribut Class
        - `tipe_pelanggan` : menyimpan tipe pelanggan.
        - `jumlah_pelanggan` : menghitung jumlah object pelanggan yang dibuat.
        - `status_pelanggan` : menyimpan status pelanggan.

        Atribut Instance
        - `nama` : nama pelanggan.
        - `__nomor_hp` : nomor HP pelanggan yang bersifat private.
        - `alamat` : alamat pelanggan.

        Instance Method
        - `tampilkan_data()` : menampilkan data pelanggan.
        - `ubah_nomor_hp(nomor_baru)` : mengubah nomor HP pelanggan.
        - `ubah_alamat(alamat_baru)` : mengubah alamat pelanggan.

        Property dan Setter
        - `nomor_hp` : digunakan untuk mengakses dan mengubah nomor HP.

        Setter melakukan validasi agar nomor HP memiliki minimal 11 digit.

        Class Method
        - `info_pelanggan()` : menampilkan informasi umum pelanggan.

        Static Method
        - `format_nomor_hp(nomor_hp)` : memformat nomor HP agar lebih mudah dibaca.

    3.3 Class `Transaksi`

        Class `Transaksi` digunakan untuk mengelola proses pembelian antara pelanggan dan produk.

        Atribut Class
        - `jumlah_transaksi` : menghitung jumlah object transaksi yang dibuat.
        - `status_transaksi` : menyimpan status transaksi.
        - `nama_toko` : menyimpan nama toko.

        Atribut Instance
        - `pelanggan` : object pelanggan yang melakukan transaksi.
        - `produk` : object produk yang dibeli.
        - `__jumlah_beli` : jumlah produk yang dibeli dan bersifat private.
        - `__total_harga` : total harga transaksi dan bersifat private.

        Instance Method
        - `hitung_total()` : menghitung total harga berdasarkan harga produk dan jumlah pembelian.
        - `proses_pembelian()` : memproses pembelian dan mengurangi stok jika stok mencukupi.
        - `tampilkan_transaksi()` : menampilkan detail transaksi.
        - `cetak_struk()` : menampilkan struk pembelian.

        Property dan Setter
        - `jumlah_beli` : digunakan untuk mengakses dan mengubah jumlah pembelian.
        - `total_harga` : digunakan untuk mengakses total harga.

        Setter `jumlah_beli` melakukan validasi agar jumlah pembelian harus lebih dari 0.

        Class Method
        - `info_transaksi()` : menampilkan informasi umum transaksi.

        Static Method
        - `format_rupiah(nilai)` : mengubah angka menjadi format mata uang Rupiah.

4. Hubungan Antar-Class

Class `Pelanggan` digunakan untuk menyimpan data pelanggan yang melakukan pembelian. Class `Produk` digunakan untuk menyimpan data barang yang tersedia di toko, termasuk stok dan harga. Class `Transaksi` menghubungkan data pelanggan dengan data produk untuk mencatat proses pembelian.

Object `Transaksi` menerima object `Pelanggan` dan object `Produk` sebagai data yang digunakan dalam transaksi. Dengan demikian, transaksi dapat mengetahui pelanggan yang melakukan pembelian, produk yang dibeli, jumlah pembelian, serta total harga.

Contoh:

'transaksi1 = Transaksi(pelanggan1, produk1, 3)'

Artinya `pelanggan1` melakukan pembelian `produk1` sebanyak 3 unit.

5. Konsep PBO yang Digunakan

    5.1 Class dan Object

    Class digunakan sebagai cetak biru untuk membuat object. Contohnya:

    produk1 = Produk("Kaca Tempered", "Kaca", 50, 150000)
    produk2 = Produk("Aluminium Frame", "Aluminium", 30, 200000)

    `produk1` dan `produk2` merupakan object dari class `Produk`.

    5.2 Encapsulation

    Encapsulation diterapkan menggunakan atribut private dengan awalan `__`.

    Contoh:

    self.__stok = stok
    self.__harga = harga

    Atribut tersebut diakses melalui property dan setter:

    @property
    def stok(self):
        return self.__stok

    Dengan cara ini, perubahan data dapat diberikan validasi sebelum disimpan.

    5.3 Instance Method

    Instance method menggunakan parameter `self` dan bekerja terhadap object tertentu.

    Contoh:

    produk1.tambah_stok(10)

    Method tersebut hanya mengubah stok milik `produk1`.

    5.4 Class Method

    Class method menggunakan decorator `@classmethod` dan parameter `cls`.

    Contoh:

    Produk.info_toko()

    Method tersebut mengakses data yang dimiliki oleh class `Produk`.

    5.5 Static Method

    Static method menggunakan decorator `@staticmethod` dan tidak membutuhkan `self` maupun `cls`.

    Contoh:

    Pelanggan.format_nomor_hp("08123456789")

    Method tersebut dapat digunakan tanpa membuat object baru.

6. Data Object yang Digunakan

Program membuat minimal dua object untuk setiap class.

Object Produk
produk1 = Produk("Kaca Tempered", "Kaca", 50, 150000)
produk2 = Produk("Aluminium Frame", "Aluminium", 30, 200000)

Object Pelanggan
pelanggan1 = Pelanggan("Aditya", "08123456789", "Samarinda")
pelanggan2 = Pelanggan("Budi", "08234567890", "Samarinda")

Object Transaksi
transaksi1 = Transaksi(pelanggan1, produk1, 3)
transaksi2 = Transaksi(pelanggan2, produk2, 5)

7. Panduan Pengujian Program

Pengujian dilakukan untuk memastikan setiap method pada ketiga class dapat berjalan.

    7.1 Pengujian Class `Produk`

    Jalankan:
    produk1.tampilkan_info()
    produk1.tambah_stok(10)
    produk1.kurangi_stok(5)

    produk2.tampilkan_info()
    produk2.tambah_stok(20)
    produk2.kurangi_stok(10)

    Pengujian ini memastikan method untuk menampilkan informasi, menambah stok, dan mengurangi stok dapat digunakan.

    7.2 Pengujian Static Method `Produk`

    Produk.cek_kebutuhan_stok(produk1.stok, 30)
    Produk.cek_kebutuhan_stok(produk2.stok, 100)

    Pengujian menggunakan dua kondisi:
    - kebutuhan stok masih mencukupi;
    - kebutuhan stok melebihi stok yang tersedia.

    7.3 Pengujian Class Method `Produk`

    Produk.info_toko()

    Method ini digunakan untuk menampilkan informasi toko dan jumlah produk.

    7.4 Pengujian Class `Pelanggan`

    pelanggan1.tampilkan_data()
    pelanggan1.ubah_nomor_hp("08111111111")
    pelanggan1.ubah_alamat("Balikpapan")

    pelanggan2.tampilkan_data()
    pelanggan2.ubah_nomor_hp("08222222222")
    pelanggan2.ubah_alamat("Samarinda")

    Pengujian memastikan data kedua pelanggan dapat ditampilkan dan diubah.

    7.5 Pengujian Static Method `Pelanggan`

    print(Pelanggan.format_nomor_hp(pelanggan1.nomor_hp))
    print(Pelanggan.format_nomor_hp(pelanggan2.nomor_hp))

    Method ini menguji proses pemformatan nomor HP.

    7.6 Pengujian Class Method `Pelanggan`

    Pelanggan.info_pelanggan()

    Method ini menampilkan informasi umum pelanggan.

    7.7 Pengujian Class `Transaksi`

    print(transaksi1.hitung_total())
    transaksi1.proses_pembelian()
    transaksi1.tampilkan_transaksi()
    transaksi1.cetak_struk()

    Kemudian transaksi kedua:

    print(transaksi2.hitung_total())
    transaksi2.proses_pembelian()
    transaksi2.tampilkan_transaksi()
    transaksi2.cetak_struk()

    Pengujian memastikan perhitungan total, proses pembelian, tampilan transaksi, dan pencetakan struk berjalan.

    7.8 Pengujian Class Method dan Static Method `Transaksi`

    Transaksi.info_transaksi()

    print(Transaksi.format_rupiah(150000))
    print(Transaksi.format_rupiah(450000))

    Pengujian ini memastikan kedua method dapat dipanggil melalui class tanpa membuat object baru.

8. Pengujian Setter

Setter diuji menggunakan data valid dan tidak valid untuk membuktikan bahwa validasi berjalan.

    8.1 Setter Stok

    produk1.stok = 100
    print(produk1.stok)

    produk1.stok = -10

    Hasil yang diharapkan:
    - nilai `100` diterima;
    - nilai `-10` ditolak karena stok tidak boleh negatif.

    8.2 Setter Harga

    produk1.harga = 175000
    print(produk1.harga)

    produk1.harga = 0

    Hasil yang diharapkan:
    - nilai `175000` diterima;
    - nilai `0` ditolak karena harga harus lebih dari 0.

    8.3 Setter Nomor HP

    pelanggan1.nomor_hp = "08133333333"
    print(pelanggan1.nomor_hp)

    pelanggan1.nomor_hp = "12345"

    Hasil yang diharapkan:
    - nomor dengan minimal 11 digit diterima;
    - nomor kurang dari 11 digit ditolak.

    8.4 Setter Jumlah Pembelian

    transaksi1.jumlah_beli = 5
    print(transaksi1.jumlah_beli)

    transaksi1.jumlah_beli = 0

    Hasil yang diharapkan:
    - nilai `5` diterima;
    - nilai `0` ditolak karena jumlah pembelian harus lebih dari 0.

9. Alur Pengujian Transaksi

Pengujian transaksi dilakukan dengan membuat object transaksi berdasarkan pelanggan dan produk yang tersedia. Setelah object transaksi dibuat, program menghitung total harga berdasarkan harga produk dan jumlah pembelian. Selanjutnya program memeriksa ketersediaan stok. Jika stok mencukupi, pembelian diproses dan stok produk dikurangi. Setelah itu, detail transaksi dan struk pembelian dapat ditampilkan.

Contoh:
transaksi1 = Transaksi(pelanggan1, produk1, 3)
transaksi1.hitung_total()
transaksi1.proses_pembelian()
transaksi1.tampilkan_transaksi()
transaksi1.cetak_struk()

10. Kesimpulan

Program ini menerapkan konsep dasar Pemrograman Berorientasi Objek untuk mengelola produk, pelanggan, dan transaksi pada Toko Kaca & Aluminium. Setiap class memiliki tanggung jawab yang berbeda sehingga pengelolaan data menjadi lebih terstruktur.

Program juga menyediakan pengujian terhadap instance method, class method, static method, serta setter menggunakan data valid dan tidak valid. Pengujian tersebut digunakan untuk memastikan fungsi program dan validasi data berjalan sesuai dengan rancangan.
