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
        usia = input("Usia: ")  
        Pendidikan_Terakhir = input("Pendidikan Terakhir: ")  
        alamat_domisili = input("Alamat Domisili: ")  
        
        for akun in akuns:
            if akun["username"] == username:
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
            
            # Menyimpan akun sebagai dictionary
            akuns.append({
                "username": username,
                "password": password,
                "kejuruan": kejuruan,
                "deadline_pendaftaran": deadline_pendaftaran,
                "lama_tempuh_pelatihan": lama_tempuh_pelatihan,
                "NIK": NIK,
                "nama_lengkap": nama_lengkap,
                "alamat_domisili": alamat_domisili,
                "riwayat_pelatihan": []  # Riwayat pelatihan sebagai list kosong
            })
            print(f"Akun Anda berhasil terdaftar dengan ID: {username}")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        username = input("Username: ")
        password = input("Password: ")
        akun_tertemukan = None
        for akun in akuns:
            if akun["username"] == username and akun["password"] == password: 
                akun_tertemukan = akun
                break
        if akun_tertemukan:
            while True:
                print(f"\nSelamat datang {username}!")
                print("―――Silakan pilih aksi!―――")
                print("1. Daftar pelatihan kerja")
                print("2. Lihat riwayat pelatihan")
                print("3. Edit profil")
                print("4. Hapus akun")
                print("5. Logout")
                print("―――――――――――――――――――――――――――――")

                status = input("Pilih opsi: ")
                print(" ")

                if status == "1":
                    print(f"NIK: {akun_tertemukan['NIK']}")
                    print(f"Nama Lengkap: {akun_tertemukan['nama_lengkap']}")
                    print(f"Alamat Domisili: {akun_tertemukan['alamat_domisili']}")
                    print(f"Username: {akun_tertemukan['username']}")
                    print(f"Kejuruan: {akun_tertemukan['kejuruan']}")
                    print(f"Deadline Pendaftaran: {akun_tertemukan['deadline_pendaftaran']}")