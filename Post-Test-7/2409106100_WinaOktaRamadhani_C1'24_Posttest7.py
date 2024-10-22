akuns = []
kejuruan_options = {
    "1": ("Pembuatan Roti dan Kue", "tanggal 1 sampai dengan 18 Februari 2024", "27 hari"),
    "2": ("Teknisi Alat Berat", "tanggal 2 sampai dengan 20 Januari 2024", "30 hari"),
}

def daftar_akun():
    "Fungsi untuk mendaftar akun baru."
    global akuns  
    print("Halo Pengguna baru! Ayo buat akun dulu")
    nama_lengkap = input("Nama Lengkap: ")
    username = input("Username: ")
    password = input("Password: ")
    NIK = input("NIK: ")  
    usia = input("Usia: ")  
    Pendidikan_Terakhir = input("Pendidikan Terakhir: ")  
    alamat_domisili = input("Alamat Domisili: ")  
    
    if any(akun["username"] == username for akun in akuns):
        print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        return
    
    print("Pilih kejuruan:")
    print("1. Pembuatan Roti dan Kue")
    print("2. Teknisi Alat Berat")
    kejuruan = input("Pilih kejuruan: ")
    
    if kejuruan in kejuruan_options:
        kejuruan_name, deadline_pendaftaran, lama_tempuh_pelatihan = kejuruan_options[kejuruan]
        akuns.append({
            "username": username,
            "password": password,
            "kejuruan": kejuruan_name,
            "deadline_pendaftaran": deadline_pendaftaran,
            "lama_tempuh_pelatihan": lama_tempuh_pelatihan,
            "NIK": NIK,
            "nama_lengkap": nama_lengkap,
            "alamat_domisili": alamat_domisili,
            "riwayat_pelatihan": [] 
        })
        print(f"Akun Anda berhasil terdaftar dengan ID: {username}")
    else:
        print("Input tidak valid, silahkan pilih 1 atau 2")

def login():
    "Fungsi untuk login ke akun."
    global akuns
    print("Hi, Silahkan login dulu ya!")
    username = input("Username: ")
    password = input("Password: ")
    
    for akun in akuns:
        if akun["username"] == username and akun["password"] == password: 
            return akun
    print("Username atau password salah!")
    return None

def tampilkan_menu(akun):
    "Fungsi untuk menampilkan menu setelah login."
    while True:
        print(f"\nSelamat datang {akun['username']}!")
        print("―――Silakan pilih aksi!―――")
        print("1. Daftar pelatihan kerja")
        print("2. Lihat riwayat pelatihan")
        print("3. Edit profil")
        print("4. Hapus akun")
        print("5. Logout")
        print("―――――――――――――――――――――――――――――")

        status = input("Pilih opsi: ")
        if status == "5":
            print("Anda telah logout.")
            break

def main():
    "Prosedur utama untuk menjalankan aplikasi."
    while True:
        print("Selamat datang di aplikasi Pendaftaran Pelatihan Kerja!")
        print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
        print("1. Daftar akun")
        print("2. Login")
        print("3. Exit")
        print("――――――――――――――――――――――――")
        opsi = input("Pilih opsi: ")

        if opsi == "1":
            daftar_akun()
        elif opsi == "2":
            akun_tertemukan = login()
            if akun_tertemukan:
                tampilkan_menu(akun_tertemukan)
        elif opsi == "3":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Input tidak valid, silahkan pilih 1, 2, atau 3")

main()