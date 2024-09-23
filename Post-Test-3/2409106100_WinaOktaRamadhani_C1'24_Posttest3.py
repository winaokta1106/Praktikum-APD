print("Nama: ")
nama = input()
print("Hari: ")
hari = input()
if hari == "Senin":
    print("Harga Tiket Rp. 40000, Masukkan Uang Anda: ")
    hargatiket = int(input())
    if hargatiket >= 40000:
        sisa = hargatiket - 40000
        print("Pembelian Tiket Anda Berhasil!!")
    else:
        kurang = 40000 - hargatiket
        print("Woopss Uang nya kurang wirr..!!")
        print("Pembelian Ttiket Gagal.")
else:
    if hari == "Selasa":
        print("Harga Tiket Rp. 40000, Masukkan Uang Anda: ")
        hargatiket = int(input())
        if hargatiket >= 40000:
            sisa = hargatiket - 40000
            print("Pembelian Tiket Anda Berhasil!!")
        else:
            kurang = 40000 - hargatiket
            print("Woopss Uang nya kurang wirr..!!")
            print("Pembelian Ttiket Gagal.")
    else:
        if hari == "Rabu":
            print("Harga Tiket Rp.40000, Masukan Uang Anda")
            hargatiket = int(input())
            if hargatiket >= 40000:
                sisa = hargatiket - 40000
                print("Pembelian Tiket Anda Berhasil!!")
            else:
                kurang = 40000 - hargatiket
                print("Woopss Uang nya kurang wirr..!!")
                print("Pembelian Ttiket Gagal.")
        else:
            if hari == "Kamis":
                print("Harga Tiket Rp.40000, Masukan Uang Anda")
                hargatiket = int(input())
                if hargatiket >= 40000:
                    sisa = hargatiket - 40000
                    print("Pembelian Tiket Anda Berhasil!!")
                else:
                    kurang = 40000 - hargatiket
                    print("Woopss Uang nya kurang wirr..!!")
                    print("Pembelian Ttiket Gagal.")
if hari == "Jum'at":
    print("Harga Tiket Rp. 40000, Masukkan Uang Anda: ")
    hargatiket = int(input())
    if hargatiket >= 45000:
        sisa = hargatiket - 45000
        print("Pembelian Tiket Anda Berhasil!!")
    else:
        kurang = 45000 - hargatiket
        print("Woopss Uang nya kurang wirr..!!")
        print("Pembelian Ttiket Gagal.")
if hari == "Sabtu":
    print("Harga Tiket Rp. 55000, Masukkan Uang Anda: ")
    hargatiket = int(input())
    if hargatiket >= 55000:
        sisa = hargatiket - 55000
        print("Pembelian Tiket Anda Berhasil!!")
        
    else:
        kurang = 55000 - hargatiket
        print("Woopss Uang nya kurang wirr..!!")
        print("Pembelian Ttiket Gagal.")
if hari == "Minggu":
    print("Harga Tiket Rp.60000, Masukkan Uang Anda")
    hargatiket = int(input())
    if hargatiket >= 60000:
        sisa = hargatiket - 60000
        print("Pembelian Tiket Anda Berhasil!!")
    else:
        kurang = 60000 - hargatiket
        print("Woopss Uang nya kurang wirr..!!")
        print("Pembelian Ttiket Gagal.")
        