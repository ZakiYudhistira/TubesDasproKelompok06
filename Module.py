# Library fungsi - fungsi program
import os, time, random

# Class MatriksData sebagai tipe data utama untuk menyimpan dan mengubah ketiga file yang digunakan.
# Tipe ini memiliki lima atribut, yaitu
# path_file: path file data yang ingin digunakan;
# nama_data: nama data yang digunakan (berguna saat pembuatan file baru);
# nparam: jumlah parameter yang terdapat pada data (sebagai jumlah kolom dalam file data dan matriks);
# nmaks: jumlah maksimum yang terdapat pada data (sebagai jumlah baris pada file data dan matriks); dan
# matriks: matriks utama tempat penyimpanan dan perubahan data (memiliki dimensi (nmax)X(nparam)).
class MatriksData:
    def __init__(self, path_file, nama_data, nparam, nmaks, matriks=None):
        self.path_file = path_file
        self.nama_data = nama_data
        self.nparam = nparam
        self.nmaks = nmaks
        self.matriks = loadData(path_file, nparam, nmaks)

Matriks = list[list[str|int]]

# =============================================== FUNGSI DAN PROSEDUR MATRIKS ================================================
# Fungsi dan prosedur yang digunakan untuk mengambil informasi ataupun mengubah informasi pada matriks secara general.

# ----------------------------------------- Fungsi panjangMatriks (credit: 16522028) -----------------------------------------
# Fungsi yang mengembalikan jumlah elemen yang terisi pada sebuah matriks.
def panjangMatriks(matriks_data:Matriks, nmaks:int) -> int:
    count = 0
    for baris in range(nmaks):
        if matriks_data[baris][0] is not None:
            count += 1
        else:
            break
        
    return count

# ------------------------------------------- Fungsi getIndeks (credit: 16522028) --------------------------------------------
# Fungsi yang mengembalikan indeks dari sebuah data yang dipilih pada sebuah matriks.
def getIndeks(matriks_data:Matriks, data:str|int, nmaks:int, i_ref=0) -> int|None:
    indeks = None
    neff = panjangMatriks(matriks_data, nmaks)
    for i in range(neff):
        if matriks_data[i][i_ref] == data:
            indeks = i
            break

    return indeks

# ------------------------------------------ Prosedur hapusData (credit: 16522028) -------------------------------------------
# Prosedur untuk menghapus data yang diinginkan pada sebuah MatriksData.
def hapusData(matriks_data:MatriksData, data:str|int, i_ref=0) -> None:
    neff = panjangMatriks(matriks_data.matriks, matriks_data.nmaks)
    i_data = getIndeks(matriks_data.matriks, data, matriks_data.nmaks, i_ref)

    for data in range(i_data, neff):
        if data != matriks_data.nmaks-1:
            matriks_data.matriks[data] = matriks_data.matriks[data+1]

    if neff == matriks_data.nmaks:
        matriks_data.matriks[neff-1] = [None for i in range(matriks_data.nparam)]


# ============================================== FUNGSI DAN PROSEDUR TEKNIS ==================================================
# Fungsi dan prosedur teknis yang digunakan pada awal dan akhir penjalanan program

# --------------------------------------------- Fungsi login (credit: 19622199) ----------------------------------------------
# Fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil.
def login(matriks_data_user:MatriksData) -> tuple[bool,str,str]:
    data_user = matriks_data_user.matriks
    user = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    for i in range(matriks_data_user.nmaks): # loop pemrosesan file csv untuk menentukan password dan username
        akses = False
        username = True
        password_p = True
        if data_user[i][0] == user:
            if data_user[i][1] == password:
                akses = True
                break
            else:
                akses = False
                password_p = False
                break
        else:
            akses = False
            username = False
            password_p = False

    if akses:
        print("Selamat Datang, "+user+"!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return akses,data_user[i][0],data_user[i][2]
    else:
        if username == True and password_p == False:
            print("Password salah!")
        elif username == False and password_p == False:
            print("Username tidak terdaftar!")
        return akses," ", " "

# --------------------------------------------- Fungsi logout (credit: 19622199) ---------------------------------------------
# Fungsi yang mengembalikan status login menjadi awal.
def logout() -> tuple[bool,str,str]:
    return False, " ", " "

# --------------------------------------- Prosedur Help (credit: 19622010 & 19622199) ----------------------------------------
# Prosedur untuk mengoutput keterangan command sesuai dengan current role pengguna.
def help(role:str) -> None:

    if role == "bandung_bondowoso":
        print("""Berikut merupakan beberapa command yang bisa Anda lakukan:
1.logout: Untuk keluar dari akun yang digunakan sekarang.
2.summonjin: Untuk memanggil jin.
3.hapusjin: Untuk menghilangkan jin.
4.ubahjin: Untuk mengubah Jin pengumpul jadi jin pembangun dan sebaliknya.
5.batchkumpul: Untuk menyuruh semua jin pengumpul mengumpulkan bahan candi.
6.batchbangun: Untuk menyuruh semua jin pembangun membuat candi.
7.laporanjin: Menunjukkan jumlah jin yang ada dan propertinya.
8.laporancandi: Menunjukkan jumlah candi yang sudah terbangung dan propertinya.
9.leaderboard: Menunjukkan leaderboard jin pembangun atau candi saat ini.""")

    elif role == "roro_jonggrang":
        print("""Berikut merupakan beberapa command yang bisa Anda lakukan:
1.logout: Untuk keluar dari akun yang digunakan sekarang.
2.ayamberkokok: Memalsukan waktu dan mengakhiri permainan.
3.hancurkancandi: Menghancurkan candi yang telah dibuat.""")

    elif role == "jin_pengumpul":
       print("""Berikut merupakan beberapa command yang bisa Anda lakukan:
1.logout: Untuk keluar dari akun yang digunakan sekarang.
2.bangun: Membangun candi dari bahan yang sudah terkumpulkan.""")

    elif role == "jin_pembangun":
        print("""Berikut merupakan beberapa command yang bisa Anda lakukan:
1.logout: Untuk keluar dari akun yang digunakan sekarang.
2.bangun: Membangun candi dari bahan yang sudah terkumpulkan.""")

# -------------------------------------------- Fungsi loadData (credit: 16522028) --------------------------------------------
# Fungsi yang mengembalikan sebuah martriks berisi data yang dibaca dengan jumlah baris nmaks dan jumlah kolom nparam.
def loadData(path_file:str, nparam:int, nmaks:int) -> Matriks:

    with open(path_file, 'r') as file:
        data_file = file.read()
        matriks_data = [[None for i in range(nparam)] for j in range(nmaks)]
        data = ''
        indeks_baris = 0
        indeks_kolom = 0

        for huruf in data_file:
            if huruf == ';' or huruf == '\n':
                if huruf != '\n':
                    if indeks_baris != 0:
                        matriks_data[indeks_baris-1][indeks_kolom] = data
                    indeks_kolom += 1
                else:
                    if indeks_baris != 0:
                        matriks_data[indeks_baris-1][indeks_kolom] = data
                    indeks_baris += 1
                    indeks_kolom = 0
                data = ''
            else:
                data += huruf

        if data != '' and indeks_baris != 0:
            matriks_data[indeks_baris-1][indeks_kolom] = data

    return matriks_data

# ---------------------------------------- Fungsi tulisMatriksData (credit: 16522028) ----------------------------------------
# Fungsi yang mengembalikan string berisi data setiap MatriksData dengan format yang sama dengan isi file eksternal.
def tulisMatriksData(matriks_data:MatriksData) -> str:
    neff = panjangMatriks(matriks_data.matriks, matriks_data.nmaks)

    if matriks_data.nama_data == "user":
        string_data = "username;password;role"
    elif matriks_data.nama_data == "candi":
        string_data = "id;pembuat;pasir;batu;air"
    elif matriks_data.nama_data == "bahan_bangunan":
        string_data = "nama;deskripsi;jumlah"

    if neff != 0:
        string_data += '\n'

    for baris in range(neff):
        for param in range(matriks_data.nparam):
            if param != (matriks_data.nparam - 1):
                string_data = string_data + matriks_data.matriks[baris][param] + ';'
            else:
                if baris != (neff - 1):
                    string_data = string_data + matriks_data.matriks[baris][param] + '\n'
                else:
                    string_data = string_data + matriks_data.matriks[baris][param]

    return string_data

# ------------------------------------------- Prosedur saveFile (credit: 16522028) -------------------------------------------
# Prosedur untuk menyimpan file berdasarkan path dan data yang diberikan.
def saveFile(path:str, data:str) -> None:
    with open(path, 'w') as file:
        file.write(data)

# ------------------------------------------- Prosedur saveData (credit: 16522028) -------------------------------------------
# Prosedur untuk menyimpan data yang telah digunakan ke sebuah folder eksternal.
def saveData(data:tuple[list[MatriksData]|int]) -> None:
    nama_folder = input("Masukkan nama folder: ")
    parent_folder = "save"
    dotdotdot("Saving", 3, 0.5)
    
    save_directory = f"{parent_folder}\\{nama_folder}"
    for i in range(len(save_directory)):

        if save_directory[i] == '/' or save_directory[i] == '\\' or i == (len(save_directory) - 1):
            if not os.path.exists(save_directory):
                dotdotdot(f"Membuat folder {save_directory}", 3, 0.5)
                os.makedirs(save_directory)
                time.sleep(0.5)

    for i in range(data[1]):
        saveFile(f"{save_directory}\\{data[0][i].nama_data}.csv", tulisMatriksData(data[0][i]))

    time.sleep(0.5)
    print(f"Berhasil menyimpan data di folder {save_directory}!")


# =============================================== FUNGSI DAN PROSEDUR GENERAL ================================================
# Fungsi dan prosedur yang digunakan pada fungsi dan prosedur lainnya serta tidak terkhususkan pada suatu role

# ------------------------------------------ Prosedur dotdotdot (credit: 16522028) -------------------------------------------
# Prosedur mengoutput teks dengan dot dot dot yang dramatis.
def dotdotdot(teks:str, n_dot:int, interval:int) -> None:
    print(teks, end="", flush=True)
    time.sleep(interval)
    for i in range(n_dot):
        print('.', end="", flush=True)
        time.sleep(interval)
    print()

# ------------------------------------------- Fungsi jumlahBahan (credit: 16522028)-------------------------------------------
# Fungsi yang mengembalikan 3 data bahan (pasir, batu, air) berdasarkan data pada matriks_bahan.
def jumlahBahan(matriks_candi:MatriksData) -> tuple[int, int, int]:
    pasir, batu, air = 0, 0, 0
    neff = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)

    for candi in range(neff):
        pasir += int(matriks_candi.matriks[candi][2])
        batu += int(matriks_candi.matriks[candi][3])
        air += int(matriks_candi.matriks[candi][4])

    return pasir, batu, air

# ------------------------------------------- Fungsi jumlahJin (credit: 16522028) --------------------------------------------
# Fungsi yang mengembalikan 3 data total jin (total, pengumpul, pembangun) berdasarkan data pada matriks_user.
def jumlahJin(matriks_user:MatriksData) -> tuple[int, int, int]:
    jumlah_jin, jumlah_pengumpul, jumlah_pembangun = 0, 0, 0
    neff = panjangMatriks(matriks_user.matriks, matriks_user.nmaks)

    for jin in range(2, neff):
        jumlah_jin += 1
        if matriks_user.matriks[jin][2] == "jin_pengumpul":
            jumlah_pengumpul += 1
        else:
            jumlah_pembangun += 1

    return jumlah_jin, jumlah_pengumpul, jumlah_pembangun

# ----------------------------------------- Fungsi generateBahan (credit: 19622199) ------------------------------------------
# Fungsi yang akan mengembalikan 3 nilai int yang merepresentasikan nilai pasir, batu, dan air.
def generateBahan() -> tuple[int ,int ,int]:
    pasir = random.randint(1,5)
    batu = random.randint(1,5)
    air = random.randint(1,5)
    return pasir,batu,air


# ============================================== FUNGSI DAN PROSEDUR BONDOWOSO ===============================================
# Fungsi dan prosedur yang hanya bisa digunakan oleh Bondowoso

# ------------------------------------------- Prosedur printJin (credit: 19622199) -------------------------------------------
# Prosedur untuk mengoutput tulisan saat jin disummon, dihapus, atau diganti.
def printJin(nama:str,jenis:str) -> None:
    if jenis == "summon":
        dotdotdot("Mengumpulkan sesajen", 3, 0.3)
        dotdotdot("Menyerahkan sesajen", 3, 0.3)
        dotdotdot("Membacakan mantra", 3, 0.3)
        print(f"Jin {nama} berhasil dipanggil!")
    elif jenis == "hapus":
        dotdotdot(f"Dicari jin {nama}", 3, 0.3)
        dotdotdot(f"Telah ditangkap jin {nama}", 3, 0.3)
        dotdotdot("Membacakan mantra", 3, 0.3)
        print("Jin telah berhasil dihapus dari alam gaib.")
    elif jenis == "ganti":
        dotdotdot(f"Dicari jin {nama}", 3, 0.3)
        dotdotdot(f"Telah ditangkap jin {nama}", 3, 0.3)
        dotdotdot("Membacakan mantra", 3, 0.3)
        print("Jin telah berhasil diubah.")

# ------------------------------------------- Fungsi cekNamajin (credit: 19622199) -------------------------------------------
# Fungsi untuk melakukan pengecekan apakah suatu nama jin sudah terdaftar atau belum.
def cekNamaJin(matriks_user:MatriksData,nama_jin:str) -> bool:
    for i in range(matriks_user.nmaks):
        if nama_jin == matriks_user.matriks[i][0]:
            return True
    return False

# --------------------------------------- Fungsi cekPanjangPassword (credit: 19622199) ---------------------------------------
# Fungsi untuk memvalidasi panjang password yang sesuai.
def cekPanjangPassword(password:str) -> bool:
    char = 0
    for i in password:
        char+=1
    if char < 5 or char > 25:
        return True
    else:
        return False
    
# ----------------------------------------- Prosedur isiMatriksUser (credit: 19622199) -----------------------------------------
# Prosedur untuk mengisi data ke matriks yang telah ditentukan.
def isiMatriksUser(matriks_user:MatriksData,nama_jin:str,password_jin:str,role_jin:str) -> None:
    for i in range(matriks_user.nmaks):
        if matriks_user.matriks[i][0] == None:
            angka = i
            break
    matriks_user.matriks[angka][0],matriks_user.matriks[angka][1],matriks_user.matriks[angka][2] = nama_jin,password_jin,role_jin

# ------------------------------------------ Prosedur summonJin (credit: 19622199) -------------------------------------------
# Prosedur untuk menciptakan jin baru, akan dilakukan validasi jumlah jin terlebih dahulu.
def summonJin(matriks_user:MatriksData) -> None:
    jumlah_jin = jumlahJin(matriks_user)[0]
    print("""Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi
(3) Tidak jadi summon jin""")
    if jumlah_jin == 100:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        while True:
            nomor_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

            if nomor_jin == 1:
                dotdotdot('Memilih jin "Pengumpul"', 3, 0.5)
                nama_jin = str(input("Masukkan nama jin: "))
                while cekNamaJin(matriks_user,nama_jin):
                    print(f"Username “{nama_jin}” sudah diambil!\n")
                    nama_jin = input("Masukkan nama jin: ")

                password_jin = str(input("Masukkan password jin: "))
                while cekPanjangPassword(password_jin):
                    print("Password panjangnya harus 5-25 karakter!\n")
                    password_jin = input("Masukkan password jin: ")

                printJin(nama_jin,"summon")
                role_jin = "jin_pengumpul"
                isiMatriksUser(matriks_user,nama_jin,password_jin,role_jin)
                break

            elif nomor_jin == 2:
                dotdotdot('Memilih jin "Pembangun"', 3, 0.5)
                nama_jin = str(input("Masukkan nama jin: "))
                while cekNamaJin(matriks_user,nama_jin):
                    print(f"Username “{nama_jin}” sudah diambil!\n")
                    nama_jin = input("Masukkan nama jin: ")

                password_jin = str(input("Masukkan password jin: "))
                while cekPanjangPassword(password_jin):
                    print("Password panjangnya harus 5-25 karakter!\n")
                    password_jin = input("Masukkan password jin: ")

                printJin(nama_jin,"summon")
                role_jin = "jin_pembangun"
                isiMatriksUser(matriks_user,nama_jin,password_jin,role_jin)
                break

            elif nomor_jin == 3:
                print("Oke.")
                time.sleep(0.5)
                print("Tidak ada jin yang di-summon.")
                break
            else:
                print(f'Tidak ada jenis jin bernomor "{nomor_jin}"')

# ------------------------------------- Prosedur hapusJin (credit: 19622199 & 16522028) --------------------------------------
# Prosedur untuk menghapus jin dari matriks user utama.
def hapusJin(matriks_user:MatriksData, matriks_candi:MatriksData) -> None:
    nama_jin = input("Masukkan username jin: ")

    if cekNamaJin(matriks_user,nama_jin):

        command = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ").upper()
        while not(command == "Y" or command == "N"):
            print("Perintah tidak valid, tolong input ulang perintah.")
            command = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ").upper()

        if command == "Y":
            hapusData(matriks_user, nama_jin)
            while getIndeks(matriks_candi.matriks, nama_jin, matriks_user.nmaks, 1) is not None:
                hapusData(matriks_candi, nama_jin, 1)
            printJin(nama_jin,"hapus")
        else:
            print(f"Jin {nama_jin} tidak jadi dihapus dari alam ghaib.")

    else:
        print("Tidak ada jin dengan username tersebut.")

# ----------------------------------------- Prosedur ubahTipeJin (credit: 19622199) ------------------------------------------
# Prosedur untuk mengubah tipe suatu jin pada matriks user utama.
def ubahTipeJin(matriks_user:MatriksData) -> None:
    nama_jin = input("Masukkan username jin: ")
    if cekNamaJin(matriks_user,nama_jin):
        id_jin = getIndeks(matriks_user.matriks,nama_jin,matriks_user.nmaks)

        if matriks_user.matriks[id_jin][2] == "jin_pengumpul":
            command = input(f"Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ").upper()
            while not(command == "Y") and not(command == "N"):
                print("Perintah tidak valid, tolong input ulang perintah.")
                command = input(f"Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ").upper()
            if command == "Y":
                matriks_user.matriks[id_jin][2] = "jin_pembangun"
                printJin(nama_jin,"ganti")
            elif command == "N":
                print(f"Jin pengumpul dengan username {nama_jin} tidak jadi diganti.")

        elif matriks_user.matriks[id_jin][2] == "jin_pembangun":
            command = input(f"Jin ini bertipe Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ").upper()
            while not(command == "Y") and not(command == "N"):
                print("Perintah tidak valid, tolong input ulang perintah.")
                command = input(f"Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ").upper()
            if command == "Y":
                matriks_user.matriks[id_jin][2] = "jin_pengumpul"
                printJin(nama_jin,"ganti")
            elif command == "N":
                print(f"Jin pembangun dengan username {nama_jin} tidak jadi diganti.")
    else:
        print("Tidak ada jin dengan username tersebut.")

# ----------------------------------------- Prosedur batchKumpul (credit: 19622199) ------------------------------------------
# Prosedur yang mengerahkan jin yang ada untuk mengumpulkan bahan dasar pembuatan candi.
def batchKumpul(matriks_bahan:MatriksData, matriks_user:MatriksData) -> None:
    jumlah_jin = jumlahJin(matriks_user)[2]
    pasir_awal, batu_awal, air_awal = int(matriks_bahan.matriks[0][2]) , int(matriks_bahan.matriks[1][2]), int(matriks_bahan.matriks[2][2])
    if jumlah_jin == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        for i in range(jumlah_jin):
            kumpul(matriks_bahan,True)
        pasir_total = -1*pasir_awal + int(matriks_bahan.matriks[0][2])
        batu_total = -1*batu_awal+int(matriks_bahan.matriks[1][2])
        air_total = -1*air_awal+int(matriks_bahan.matriks[2][2])
        print(f"Mengerahkan {jumlah_jin} jin untuk mengumpulkan bahan.\nJin menemukan total {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")

# ------------------------------ Prosedur batchBangun (credit: 19622199, 19622010, & 16522028) -------------------------------
# Prosedur yang mengerahkan jin yang ada untuk mengumpulkan bahan dasar pembuatan candi.
def batchBangun(matriks_bahan:MatriksData, matriks_candi:MatriksData, matriks_user:MatriksData) -> None:
    neff_user = panjangMatriks(matriks_user.matriks, matriks_user.nmaks)
    jumlah_pembangun = jumlahJin(matriks_user)[2]

    if jumlah_pembangun == 0:
        print("Bangun candi gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        
    else:
        pasir_awal, batu_awal, air_awal = int(matriks_bahan.matriks[0][2]), int(matriks_bahan.matriks[1][2]), int(matriks_bahan.matriks[2][2])
        pasir_total, batu_total, air_total = 0, 0, 0

        # Matriks untuk menyimpan informasi bahan dan pembuatnya dari setiap pembuatan candi
        matriks_pembangun = [[None, 0, 0, 0] for i in range(jumlah_pembangun)]

        for user in range(neff_user):
            pembangun = matriks_user.matriks[user][0]
            i_kosong = panjangMatriks(matriks_pembangun, jumlah_pembangun)

            if matriks_user.matriks[user][2] == "jin_pembangun":
                matriks_pembangun[i_kosong][0] = pembangun

        # Menghitung total bahan yang diperlukan serta mengisi matriks_pembangun untuk setiap pembuat dan bahannya.
        for pembangun in range(jumlah_pembangun):
            pasir, batu, air = generateBahan()
            matriks_pembangun[pembangun][1] += pasir
            pasir_total += pasir
            matriks_pembangun[pembangun][2] += batu
            batu_total += batu
            matriks_pembangun[pembangun][3] += air
            air_total += air

        print(f"Mengerahkan {jumlah_pembangun} jin untuk membangun candi dengan total bahan {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")

        if pasir_awal >= pasir_total and batu_awal >= batu_total and air_awal >= air_total:
            for pembangun in range(jumlah_pembangun):
                jin_pembangun = matriks_pembangun[pembangun][0]
                pasir = matriks_pembangun[pembangun][1]
                batu = matriks_pembangun[pembangun][2]
                air = matriks_pembangun[pembangun][3]

                bangun(matriks_bahan, matriks_candi, jin_pembangun, pasir, batu, air, True)

            print(f"Jin berhasil membangun total {jumlah_pembangun} candi.")
            
        else:
            array_kurang = [pasir_total-pasir_awal, batu_total-batu_awal, air_total-air_awal]
            for bahan in range(3):
                if array_kurang[bahan] < 0:
                    array_kurang[bahan] = 0

            print(f"Bangun gagal. Kurang {array_kurang[0]} pasir, {array_kurang[1]} batu, dan {array_kurang[2]} air.")

# ------------------------------------------ Prosedur showBahan (credit: 19622199) -------------------------------------------
# Prosedur untuk menunjukkan bahan candi yang tersedia.
def showBahan(matriks_bahan:MatriksData) -> None:
    print(f"""Persediaan bahan candi:
Pasir: {matriks_bahan.matriks[0][2]}
Batu : {matriks_bahan.matriks[1][2]}
Air  : {matriks_bahan.matriks[2][2]}""")

# ------------------------------------------ Prosedur laporanJin (credit: 16522028) ------------------------------------------
# Prosedur untuk menuliskan laporan akhir dari semua jin yang telah membantu Bondowoso.
def laporanJin(matriks_user:MatriksData, matriks_candi:MatriksData, matriks_bahan:MatriksData) -> None:
    total_jin, total_pengumpul, total_pembangun = jumlahJin(matriks_user)
    sisa_pasir = matriks_bahan.matriks[0][2]
    sisa_batu = matriks_bahan.matriks[1][2]
    sisa_air = matriks_bahan.matriks[2][2]
    jin_terajin, jin_termalas = "-", "-"

    if total_jin > 0:
        i_maks = 0
        i_min = total_pembangun - 1
        data_jin = dataJinPembangun(matriks_user, matriks_candi, "total_candi")
        matriks_leaderboard = dataLeaderboard(matriks_user, matriks_candi, data_jin, "jin")

        if matriks_leaderboard[i_maks][0] is not None:
            jin_terajin = matriks_leaderboard[i_maks][0]

        if matriks_leaderboard[i_min][0] is not None:
            jin_termalas = matriks_leaderboard[i_min][0]

    print(f"""
Berikut merupakan laporan jin Anda:
> Total Jin: {total_jin}
> Total Jin Pengumpul: {total_pengumpul}
> Total Jin Pembangun: {total_pembangun}
> Jin Terajin: {jin_terajin}
> Jin Termalas: {jin_termalas}
> Jumlah Pasir Tersisa: {sisa_pasir} unit
> Jumlah Air Tersisa: {sisa_air} unit
> Jumlah Batu Tersisa: {sisa_batu} unit
""")

# ----------------------------------------- Prosedur laporanCandi (credit: 16522028) -----------------------------------------
# Prosedur untuk menuliskan laporan akhir dari semua candi yang berhasil dibangun Bondowoso bersama semua jinnya.
def laporanCandi(matriks_user:MatriksData, matriks_candi:MatriksData, matriks_bahan:MatriksData) -> None:
    total_candi = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
    total_pasir, total_batu, total_air = jumlahBahan(matriks_candi)
    id_termahal, id_termurah = "-", "-"
    harga_termahal, harga_termurah = "", ""

    if total_candi > 0:
        i_maks = 0
        i_min = total_candi - 1
        data_candi = dataHargaCandi(matriks_candi)
        matriks_leaderboard = dataLeaderboard(matriks_user, matriks_candi, data_candi, "candi")

        if matriks_leaderboard[i_maks][0] is not None:
            id_termahal = matriks_leaderboard[i_maks][0]
            harga_termahal = f"""({matriks_leaderboard[i_maks][1]})"""

        if matriks_leaderboard[i_min][0] is not None:
            id_termurah = matriks_leaderboard[i_min][0]
            harga_termurah = f"""({matriks_leaderboard[i_min][1]})"""
        
    print(f"""
Berikut merupakan laporan candi Anda:
> Total Candi: {total_candi}
> Total Pasir yang Digunakan: {total_pasir}
> Total Air yang Digunakan: {total_air}
> Total Batu yang Digunakan: {total_batu}
> ID Candi Termahal: {id_termahal} {harga_termahal}
> ID Candi Termurah: {id_termurah} {harga_termurah}
""")


# ================================================= FUNGSI DAN PROSEDUR JIN ==================================================
# Fungsi dan prosedur yang hanya bisa digunakan oleh Jin Pengumpul dan Pembangun

# ------------------------------------------ Prosedur ubahBahan (credit: 19622199) -------------------------------------------
# Prosedur untuk mengubah nilai bahan pada matriks bahan.
def ubahBahan(matriks_bahan:MatriksData,pasir:int,batu:int,air:int) -> None:
    for i in range(matriks_bahan.nmaks):
        if matriks_bahan.matriks[i][0] == "pasir":
            bahan = int(matriks_bahan.matriks[i][2])
            matriks_bahan.matriks[i][2] = str(pasir+bahan)
        elif matriks_bahan.matriks[i][0] == "batu":
            bahan = int(matriks_bahan.matriks[i][2])
            matriks_bahan.matriks[i][2] = str(batu+bahan)
        elif matriks_bahan.matriks[i][0] == "air":
            bahan = int(matriks_bahan.matriks[i][2])
            matriks_bahan.matriks[i][2] = str(air+bahan)

# -------------------------------------------- Prosedur kumpul (credit: 19622199) --------------------------------------------
# Prosedur untuk mengumpulkan bahan dasar pembuatan candi.
def kumpul(matriks_bahan:MatriksData, batch:bool) -> None:
    pasir,batu,air = generateBahan()
    ubahBahan(matriks_bahan,pasir,batu,air)
    if not(batch):
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")

# -------------------------------------- Prosedur bangun (credit: 19622199 & 16522028) ---------------------------------------
# Prosedur untuk membangun candi dan mengeluarkan nilai boolean untuk mengindikasikan keberhasilan pembangunan candi.
def bangun(matriks_bahan:MatriksData, matriks_candi:MatriksData, jin_pembangun:str, pasir:int, batu:int, air:int, batch=False):
    nmaks = matriks_candi.nmaks
    neff = panjangMatriks(matriks_candi.matriks, nmaks)
    jumlah_candi = neff
    i_kosong = neff
    sisa_candi = nmaks - neff

    for id in range(nmaks):
        if getIndeks(matriks_candi.matriks, str(id), nmaks) is None:
            id_candi = str(id)
            break
    
    if int(matriks_bahan.matriks[0][2]) >= pasir and int(matriks_bahan.matriks[1][2]) >= batu and int(matriks_bahan.matriks[2][2]) >= air:

        ubahBahan(matriks_bahan,pasir*-1,batu*-1,air*-1)

        if jumlah_candi != 100:
            matriks_candi.matriks[i_kosong][0] = id_candi
            matriks_candi.matriks[i_kosong][1] = jin_pembangun
            matriks_candi.matriks[i_kosong][2] = str(pasir)
            matriks_candi.matriks[i_kosong][3] = str(batu)
            matriks_candi.matriks[i_kosong][4] = str(air)
            sisa_candi -= 1
        if not(batch):
            print(f"Candi berhasil dibangun!\nSisa candi yang perlu dibangun: {sisa_candi}")
    else:
        if not(batch):
            print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!")


# ================================================= FUNGSI DAN PROSEDUR RORO =================================================
# Fungsi dan prosedur yang hanya bisa digunakan oleh beloved Roro.

# ----------------------------------------- Prosedur ayamBerkokok (credit: 16522028) -----------------------------------------
# Prosedur untuk mengakhiri permainan dan menentukan pemenang berdasarkan jumlah candi yang berhasil dibuat.
def ayamBerkokok(matriks_candi:MatriksData) -> None:
    jumlah_candi = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
    print("Kukuruyuk..", end=" ", flush=True)
    time.sleep(0.5)
    print("Kukuruyuk..\n", flush=True)
    time.sleep(0.5)
    print(f"Jumlah candi: {jumlah_candi}\n")
    time.sleep(1)

    if jumlah_candi < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        dotdotdot("", 3, 0.5)
        print("*Bandung Bondowoso angry noises*\nRoro Jonggrang dikutuk menjadi candi!")
        
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")

# ---------------------------------------- Prosedur hancurkanCandi (credit: 16522028) ----------------------------------------
# Prosedur untuk menghancurkan candi berdasarkan id yang diinginkan Roro.
def hancurkanCandi(matriks_candi:MatriksData) -> None:
    id = input("Masukkan ID candi: ")
    indeks = getIndeks(matriks_candi.matriks, id, matriks_candi.nmaks)

    if indeks is None:
        print("Tidak ada candi dengan ID tersebut.")
    else:
        opsi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()
        while not(opsi == "Y" or opsi == "N"):
            print("Perintah tidak valid, tolong input ulang perintah.")
            opsi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()
        if opsi == "Y":
            hapusData(matriks_candi, id)
            print("Candi telah berhasil dihancurkan.")
        else:
            print("Understandable, have a nice day.")


# ================================================ FUNGSI DAN PROSEDUR BONUS =================================================
# Fungsi dan prosedur yang ditambahkan sebagai bonus.

# ----------------------------------------- Fungsi isTerurutLeksi (credit: 16522028) -----------------------------------------
# Fungsi yang mengembalikan nilai True jika kedua kata terurut secara leksikografis.
def isTerurutLeksi(kata1:str, kata2:str) -> bool:
    terurut = True

    if len(kata1) > len(kata2):
        ref_len = len(kata2)
    else:
        ref_len = len(kata1)

    for i_huruf in range(ref_len):
        if kata1[i_huruf] != kata2[i_huruf]:
            if kata1[i_huruf] > kata2[i_huruf]:
                terurut = False
            break

        if i_huruf == ref_len - 1:
            if ref_len == len(kata2):
                terurut = False            

    return terurut

# ---------------------------------------- Fungsi dataJinPembangun (credit: 16522028) ----------------------------------------
# Fungsi yang Mengembalikan matriks berisi data setiap jin pembangun untuk setiap kategori.
def dataJinPembangun(matriks_user:MatriksData, matriks_candi:MatriksData, kategori:str) -> Matriks:
    neff_user = panjangMatriks(matriks_user.matriks, matriks_user.nmaks)
    neff_candi = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
    nmaks_pembangun = jumlahJin(matriks_user)[2]
    matriks_data_pembangun = [[None, 0] for i in range(nmaks_pembangun)]

    for user in range(neff_user):
        pembangun = matriks_user.matriks[user][0]
        i_kosong = panjangMatriks(matriks_data_pembangun, nmaks_pembangun)

        if matriks_user.matriks[user][2] == "jin_pembangun":
            matriks_data_pembangun[i_kosong][0] = pembangun

    if kategori == "total_pasir":
        i_ref = 2
    elif kategori == "total_batu":
        i_ref = 3
    elif kategori == "total_air":
        i_ref = 4

    for candi in range(neff_candi):
        pembangun = matriks_candi.matriks[candi][1]
        i_pembuat = getIndeks(matriks_data_pembangun, pembangun, nmaks_pembangun)

        if i_pembuat is not None:
            if kategori == "total_candi":
                matriks_data_pembangun[i_pembuat][1] += 1
            elif kategori == "total_bahan":
                total_bahan = 0
                for i in range(3):
                    total_bahan += int(matriks_candi.matriks[candi][i+2])
                matriks_data_pembangun[i_pembuat][1] += total_bahan
            else:
                matriks_data_pembangun[i_pembuat][1] += int(matriks_candi.matriks[candi][i_ref])

    return matriks_data_pembangun

# ----------------------------------------- Fungsi dataHargaCandi (credit: 16522028) -----------------------------------------
# Fungsi yang mengembalikan matriks berisi data total harga yang diperlukan untuk setiap candi.
def dataHargaCandi(matriks_candi:MatriksData) -> Matriks:
    neff_candi = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
    matriks_data_harga = [[None, None] for i in range(neff_candi)]

    for candi in range(neff_candi):
        id_candi = matriks_candi.matriks[candi][0]
        pasir = int(matriks_candi.matriks[candi][2])
        batu = int(matriks_candi.matriks[candi][3])
        air = int(matriks_candi.matriks[candi][4])
        harga = pasir*10000 + batu*15000 + air*7500

        matriks_data_harga[candi] = [id_candi, harga]

    return matriks_data_harga

# ---------------------------------------- Fungsi dataLeaderboard (credit: 16522028) -----------------------------------------
# Fungsi yang mengembalikan matriks_leaderboard yang sudah terurut dari tertinggi ke terendah.
def dataLeaderboard(matriks_user:MatriksData, matriks_candi:MatriksData, matriks_leaderboard:Matriks, tipe:str) -> Matriks:
    if tipe == "jin":
        neff = jumlahJin(matriks_user)[2]
    elif tipe == "candi":
        neff = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)

    for i in range(1, neff):
        indeks = i 

        while indeks > 0 and matriks_leaderboard[indeks][1] >= matriks_leaderboard[indeks-1][1]:

            if matriks_leaderboard[indeks][1] != matriks_leaderboard[indeks-1][1]:
                temp = matriks_leaderboard[indeks]
                matriks_leaderboard[indeks] = matriks_leaderboard[indeks-1]
                matriks_leaderboard[indeks-1] = temp

            else:
                if not(isTerurutLeksi(matriks_leaderboard[indeks-1][0], matriks_leaderboard[indeks][0])):
                    temp = matriks_leaderboard[indeks]
                    matriks_leaderboard[indeks] = matriks_leaderboard[indeks-1]
                    matriks_leaderboard[indeks-1] = temp

            indeks -= 1

    return matriks_leaderboard

# --------------------------------------- Prosedur printLeaderboard (credit: 16522028) ---------------------------------------
# Prosedur untuk menuliskan leaderboard berdasarkan tipe dan kategori yang diberikan.
def printLeaderboard(matriks_user:MatriksData, matriks_candi:MatriksData) -> None:

    tipe = input("Leaderboard tipe apakah yang Anda inginkan? (jin/candi) ")

    while not(tipe == "jin" or tipe == "candi"):
        print("Tipe yang tersedia hanyalah \"jin\" atau \"candi\". Tolong ulangi kembali.")
        tipe = input("Leaderboard tipe apakah yang diinginkan? (jin/candi) ")
    
    if tipe == "candi":
        neff = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
        data_candi = dataHargaCandi(matriks_candi)
        matriks_leaderboard = dataLeaderboard(matriks_user, matriks_candi, data_candi, tipe)

        if neff != 0:
            print("Berikut merupakan leaderboard candi saat ini berdasarkan total harga:")
            for data in range(neff):
                print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")
                time.sleep(0.1)
        else:
            print("Oh maaf, data yang tersedia kosong!")

    else:
        neff = jumlahJin(matriks_user)[2]
        kategori = input("""Berikut merupakan beberapa kategori leaderboard jin pembangun:
(1): total candi yang dibuat.
(2): total bahan yang digunakan.
(3): total pasir yang digunakan.
(4): total batu yang digunakan.
(5): total air yang digunakan.
Berdasarkan kategori apakah Anda ingin melihat leaderboard jin pembangun? (1--5) """)
        while not(kategori == "1" or kategori == "2" or kategori == "3" or kategori == "4" or kategori == "5"):
            print("Kategori yang tersedia hanya ada 5. Tolong ulangi kembali.")
            kategori = input("Pada kategori apakah Anda ingin melihat leaderboard jin pembangun? (1--5) ")

        if kategori == "1":
            kategori = "total_candi"
        elif kategori == "2":
            kategori = "total_bahan"
        elif kategori == "3":
            kategori = "total_pasir"
        elif kategori == "4":
            kategori = "total_batu"
        elif kategori == "5":
            kategori = "total_air"

        data_jin = dataJinPembangun(matriks_user, matriks_candi, kategori)
        matriks_leaderboard = dataLeaderboard(matriks_user, matriks_candi, data_jin, tipe)

        if neff != 0:
            print(f"Berikut merupakan leaderboard jin pembangun saat ini berdasarkan {kategori}:")
            for data in range(neff):
                print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")
                time.sleep(0.1)
        else:
            print("Oh maaf, data yang tersedia kosong!")

