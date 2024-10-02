akuns = []

while True:
    print("Halo! selamat datang di aplikasi Catatan")
    print("Silahkan pilih 'Daftar akun'jika belum buat aku, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("____________________________")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        for akun in akuns:
            if akun[0] == Username: # Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            akuns,append([Username, Password, []]) # Simpan username, password, dan catatan (sebagai list kosong)
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")

    