akuns = []

while True:
    print("Selamat datang di aplikasi Pendaftaran Pelatihan Kerja!")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        nama_lengkap = input("Nama Lengkap: ")
        username = input("Username: ")
        akuna = False
        password = input("Password: ")
        NIK = input("NIK: ")  
        alamat_domisili = input("Alamat Domisili: ")  
        
        for akun in akuns:
            if akun[0] == username:
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            print("Pilih kejuruan:")
            print("1. Pembuatan Roti dan Kue")
            print("2. Teknisi Alat Berat")
            kejuruan = input("Pilih kejuruan: ")
            if kejuruan == "1":
                kejuruan = "Pembuatan Roti dan Kue"
                deadline_pendaftaran = "tanggal 1 sampai dengan 18 Februari 2024"
                lama_tempuh_pelatihan = "27 hari"
            elif kejuruan == "2":
                kejuruan = "Teknisi Alat Berat"
                deadline_pendaftaran = "tanggal 2 sampai dengan 20 Januari 2024"
                lama_tempuh_pelatihan = "30 hari"
            else:
                print("Input tidak valid, silahkan pilih 1 atau 2")
                continue
            akuns.append([username, password, kejuruan, deadline_pendaftaran, lama_tempuh_pelatihan, NIK, nama_lengkap, alamat_domisili, []])  # Catatan pelatihan kerja sebagai list kosong
            print(f"Akun Anda berhasil terdaftar dengan ID: {username}")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        username = input("Username: ")
        password = input("Password: ")
        akun_tertemukan = None
        for akun in akuns:
            if akun[0] == username and akun[1] == password: 
                akun_tertemukan = akun
                break
        if akun_tertemukan:
            while True:
                print(f"\nSelamat datang {username}!")
                print("―――Silakan pilih aksi!―――")
                print("2. Daftar pelatihan kerja")
                print("3. Lihat riwayat pelatihan")
                print("4. Edit profil")
                print("5. Hapus akun")
                print("6. Logout")
                print("―――――――――――――――――――――――――――――")

                status = input("Pilih opsi: ")
                print(" ")

                if status == "1":
                    print(f"NIK: {akun_tertemukan[5]}")
                    print(f"Nama Lengkap: {akun_tertemukan[6]}")
                    print(f"Alamat Domisili: {akun_tertemukan[7]}")
                    print(f"Username: {akun_tertemukan[0]}")
                    print(f"Kejuruan: {akun_tertemukan[2]}")
                    print(f"Deadline Pendaftaran: {akun_tertemukan[3]}")
                    print(f"Lama Tempuh Pelatihan: {akun_tertemukan[4]}")

                elif status == "2":
                    pelatihan_kerja = input("Nama pelatihan kerja: ")
                    akun_tertemukan[8].append([pelatihan_kerja])  
                    print("Pelatihan kerja berhasil didaftarkan!\n")

                elif status == "3":
                    if akun_tertemukan[8]:
                        for indeks, pelatihan in enumerate(akun_tertemukan[8]):
                            print(f"{indeks + 1}. {pelatihan[0]}")
                    else:
                        print("Opps, saat ini kamu belum punya riwayat pelatihan, silahkan daftar pelatihan kerja terlebih dahulu.\n")

                elif status == "4":
                    print("Edit Profil:")
                    akun_tertemukan[6] = input(f"Nama Lengkap ({akun_tertemukan[6]}): ") or akun_tertemukan[6]
                    akun_tertemukan[5] = input(f"NIK ({akun_tertemukan[5]}): ") or akun_tertemukan[5]
                    akun_tertemukan[7] = input(f"Alamat Domisili ({akun_tertemukan[7]}): ") or akun_tertemukan[7]
                    akun_tertemukan[0] = input(f"Username ({akun_tertemukan[0]}): ") or akun_tertemukan[0]
                    akun_tertemukan[1] = input(f"Password ({akun_tertemukan[1]}): ") or akun_tertemukan[1]
                    print("Profil berhasil diperbarui.\n")

                elif status == "5":
                    confirm = input("Apakah Anda yakin ingin menghapus akun ini? (y/n): ")
                    if confirm.lower() == 'y':
                        akuns.remove(akun_tertemukan)
                        print("Akun berhasil dihapus.\n")
                        break  

                elif status == "6":
                    print("Logout berhasil.\n")
                    break
        else:
            print("Username atau password salah, coba lagi.")

    elif opsi == "3":
        print("Terima kasih telah menggunakan aplikasi kami!")
        break
    else:
        print("Input tidak valid, silakan pilih opsi yang tersedia.")