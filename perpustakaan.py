print("""
      ________________________
      |======================|
      |==== PERPUSTAKAAN ====|
      |======================|
      |KODE BUKU | JENIS BUKU|
      |----------|-----------|
      |    C     |   CERPEN  |
      |    K     |   KOMIK   |
      |    N     |   NOVEL   |
      |==========|===========|
    """)
nama_penyewa = input("Masukkan Nama Penyewa : ")
kode_buku = input("Masukkan Kode Buku : ")
banyak = int(input("Jumlah Buku Yang Dipinjam : "))


if kode_buku == "C" or kode_buku == "c":
    jenis_buku = "Cerpen"
    tarif_buku = 1000
    bayar = banyak * tarif_buku
    print(f"""
      Nama Penyewa : {nama_penyewa}
      Jenis Buku : {jenis_buku}
      Jumlah Buku : {banyak}
      Tarif sewa : Rp.{tarif_buku} /Buku
      Biaya Sewa : Rp.{bayar}
      """)
elif kode_buku == "K" or kode_buku == "k":
    jenis_buku = "Komik"
    tarif_buku = 1500
    bayar = banyak * tarif_buku
    print(f"""
      Nama Penyewa : {nama_penyewa}
      Jenis Buku : {jenis_buku}
      Jumlah Buku : {banyak}
      Tarif sewa : Rp.{tarif_buku} /Buku
      Biaya Sewa : Rp.{bayar}
      """)
elif kode_buku == "N" or kode_buku == "n":
    jenis_buku = "Novel"
    tarif_buku = 2000
    bayar = banyak * tarif_buku
    print(f"""
        Nama Penyewa : {nama_penyewa}
        Jenis Buku : {jenis_buku}
        Jumlah Buku : {banyak}
        Tarif sewa : Rp.{tarif_buku} /Buku
        Biaya Sewa : Rp.{bayar}
        """)
else:
    print("Kode Buku Tidak ditemukan")

