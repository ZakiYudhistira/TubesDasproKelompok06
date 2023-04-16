# Library fungsi - fungsi program
import os, time, random

filepath = os.path.dirname(os.path.realpath(__file__))

class MatriksData:
    def __init__(self, nama_file, nama_data, n_param, n_maks, matriks = None):
        self.nama_file = nama_file
        self.nama_data = nama_data
        self.n_param = n_param
        self.n_maks = n_maks
        self.matriks = load_data(nama_file, n_param, n_maks)


#-------------------------------------------------Fungsi save_file-----------------------------------------------------------
# Procedure untuk menyimpan file berdasarkan path dan data yang diberikan.
def save_file(path:str, data:str):
    with open(path, 'w') as file:
        file.write(data)


#-------------------------------------------------Fungsi save_file-----------------------------------------------------------
# Procedure mengoutput teks dengan dot dot dot yang dramatis.
def dotdotdot(teks:str, n_dot:int, interval:int):
    print(teks, end="", flush=True)
    time.sleep(interval)
    for i in range(n_dot):
        print('.', end="", flush=True)
        time.sleep(interval)
    print()


#-------------------------------------------------Fungsi panjang_matriks-----------------------------------------------------------
# Mengembalikan panjang matriks_data yang terisi.
def panjang_matriks(matriks_data, n_maks):
    count = 0
    for baris in range(n_maks):
        if matriks_data[baris][0] is not None:
            count += 1
        else:
            break
        
    return count


#-------------------------------------------------Fungsi getIndeks-----------------------------------------------------------
# Fungsi yang mengembalikan indeks dari sebuah data yang dipilih pada sebuah matriks.
def getIndeks(matriks_data, id, n_maks:int):
    indeks = None
    neff = panjang_matriks(matriks_data, n_maks)
    for i in range(neff):
        if matriks_data[i][0] == id:
            indeks = i

    return indeks


#-------------------------------------------------Fungsi jumlahBahan-----------------------------------------------------------
# Fungsi yang mengembalikan 3 data bahan (pasir, batu, air) pada data bahan_bangunan.
def jumlahBahan(matriks_candi:MatriksData):
    pasir, batu, air = 0, 0, 0

    for candi in range(panjang_matriks(matriks_candi.matriks, matriks_candi.n_maks)):
        pasir += int(matriks_candi.matriks[candi][2])
        batu += int(matriks_candi.matriks[candi][3])
        air += int(matriks_candi.matriks[candi][4])

    return pasir, batu, air


#-------------------------------------------------Fungsi jumlahJin-----------------------------------------------------------
# Fungsi yang mengembalikan 3 data total jin (total, pengumpul, pembangun) pada data user.
def jumlahJin(matriks_user:MatriksData):
    jumlah_jin, jumlah_pengumpul, jumlah_pembangun = 0, 0, 0

    for jin in range(2, panjang_matriks(matriks_user.matriks, matriks_user.n_maks)):
        jumlah_jin += 1
        if matriks_user.matriks[jin][2] == "jin_pengumpul":
            jumlah_pengumpul += 1
        else:
            jumlah_pembangun += 1

    return jumlah_jin, jumlah_pengumpul, jumlah_pembangun


#-------------------------------------------------Fungsi login-----------------------------------------------------------
# Fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil.
def login(matriks_data_user):
    data_user = matriks_data_user.matriks
    user = input("Masukkan username : ")
    password = input("Masukkan password : ")
    
    for i in range(matriks_data_user.n_maks): # loop pemrosesan file csv untuk menentukan password dan username
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
    else :
        if username == True and password_p == False:
            print("Password salah!")
        elif username == False and password_p == False:
            print("Username tidak terdaftar!")
        return akses," ", " "

#----------------------------------------------FUNGSI Help------------------------------------------------
#Mengoutput keterangan command sesuai dengan current role pengguna
def help(role):
    list_function_bondowoso= {
    'logout': 'Untuk keluar dari akun yang digunakan sekarang',
    'summonjin': 'Untuk memanggil jin',
    'hapusjin': 'Untuk menghilangkan jin',
    'ubahjin': 'Untuk mengubah Jin pengumpul jadi jin pembangun dan sebaliknya',
    'batchkumpul': 'Untuk menyuruh semua jin pengumpul mengumpulkan bahan candi',
    'batchbangun': 'Untuk menyuruh semua jin pembangun membuat candi',
    'laporanjin': 'Menunjukkan jumlah jin yang ada dan propertinya',
    'laporancandi': 'Menunjukkan jumlah candi yang sudah terbangung dan propertinya'
    }
    list_function_rorojongrang= {
    'logout': 'Untuk keluar dari akun yang digunakan sekarang',
    'ayamberkokok': 'Memalsukan waktu dan mengakhiri permainan',
    'hancurkancandi': 'Menghancurkan candi yang telah dibuat'
    }
    list_function_jinpembangun={
    'logout': 'Untuk keluar dari akun yang digunakan sekarang',
    'bangun': 'Membangun candi dari bahan yang sudah terkumpulkan'
    }
    list_function_jinpengumpul={
    'logout': 'Untuk keluar dari akun yang digunakan sekarang',
    'kumpul': 'Mengumpulkan bahan bangunan candi'
    }

    if role == "bandung_bondowoso":
        idx=0
        for fngsi, keterangan in list_function_bondowoso.items():
            idx+=1
            print(f'{idx}.{fngsi}: {keterangan}')
        idx=0

    elif role == "roro_jonggrang":
        idx=0
        for fngsi, keterangan in list_function_rorojongrang.items():
            idx+=1
            print(f'{idx}.{fngsi}: {keterangan}')
        idx=0

    elif role == "jin_pengumpul":
        idx=0
        for fngsi, keterangan in list_function_jinpengumpul.items():
            idx+=1
            print(f'{idx}.{fngsi}: {keterangan}')
        idx=0

    elif role == "jin_pembangun":
        idx=0
        for fngsi, keterangan in list_function_jinpembangun.items():
            idx+=1
            print(f'{idx}.{fngsi}: {keterangan}')
        idx=0
#-------------------------------------------------Fungsi logout-----------------------------------------------------------
def logout():
    return False, " ", " "



#-------------------------------------------------Fungsi load_data-----------------------------------------------------------
# Mengembalikan sebuah martriks berisi data yang dibaca dengan jumlah baris n_maks dan jumlah kolom n_param.
def load_data(nama_file:str, n_param:int, n_maks:int):

    with open(nama_file, 'r') as file:
        data_file = file.read()
        matriks_data = [[None for i in range(n_param)] for j in range(n_maks)]
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


#-------------------------------------------------Fungsi tulis_matriks_data-----------------------------------------------------------
# Mengembalikan string berisi data setiap MatriksData dengan format yang sama dengan isi file eksternal.
def tulis_matriks_data(matriks_data:MatriksData):
    if matriks_data.nama_data == "user":
        string_data = "username;password;role"
    elif matriks_data.nama_data == "candi":
        string_data = "id;pembuat;pasir;batu;air"
    elif matriks_data.nama_data == "bahan_bangunan":
        string_data = "nama;deskripsi;jumlah"

    if panjang_matriks(matriks_data.matriks, matriks_data.n_maks) != 0:
        string_data += '\n'

    for baris in range(panjang_matriks(matriks_data.matriks, matriks_data.n_maks)):
        for param in range(matriks_data.n_param):
            if param != (matriks_data.n_param - 1):
                string_data = string_data + matriks_data.matriks[baris][param] + ';'
            else:
                if baris != (panjang_matriks(matriks_data.matriks, matriks_data.n_maks) - 1):
                    string_data = string_data + matriks_data.matriks[baris][param] + '\n'
                else:
                    string_data = string_data + matriks_data.matriks[baris][param]


    return string_data


#-------------------------------------------------Fungsi save_data-----------------------------------------------------------
# Procedure untuk menyimpan data yang telah digunakan ke sebuah folder eksternal.
def save_data(data:tuple):
    nama_folder = input("Masukkan nama folder: ")
    parent_folder = "save"
    dotdotdot("Saving", 3, 0.5)
    
    save_directory = f"{parent_folder}\\{nama_folder}"
    for i in range(len(save_directory)):

        if save_directory[i] == '/' or save_directory[i] == '\\' or i == (len(save_directory) - 1):
            if not os.path.exists(save_directory):
                dotdotdot(f"Membuat folder {save_directory}", 3, 0.5)
                os.makedirs(f"{filepath}\\{save_directory}")
                time.sleep(0.5)

    for i in range(data[1]):
        save_file(f"{save_directory}\\{data[0][i].nama_data}.csv", tulis_matriks_data(data[0][i]))

    time.sleep(0.5)
    print(f"Berhasil menyimpan data di folder {save_directory}!")


def cekNamaJin(file_user_utama,nama_jin):
    file_user = file_user_utama.matriks
    for i in range(file_user_utama.n_maks):
        if nama_jin == file_user[i][0]:
            return True
    return False


def getIdJin(file_user_utama,nama_jin):
    file_user = file_user_utama.matriks
    for i in range(file_user_utama.n_maks):
        if nama_jin == file_user[i][0]:
            return i


def cekPanjangPassword (password):
    char = 0
    for i in password:
        char+=1
    if char < 5 or char > 25:
        return True
    else:
        return False


def cekJumlahJin(file_user):
    if type(file_user[101][0]) == None:
        return True
    else:
        return False


def printSummon(nama):
    print("Mengumpulkan sesajen...")
    time.sleep(0.5)
    print("Menyerahkan sesajen...")
    time.sleep(0.5)
    print("Membacakan mantra...")
    time.sleep(0.5)
    print(f"Jin {nama} berhasil dipanggil!")


def printHapus(nama):
    print(f"Dicari jin {nama}...")
    time.sleep(0.5)
    print(f"Telah ditangkap jin {nama}...")
    time.sleep(0.5)
    print("Membacakan mantra...")
    time.sleep(0.5)
    print("Jin telah berhasil dihapus dari alam gaib.")


def printGanti(nama):
    print(f"Dicari jin {nama}...")
    time.sleep(0.5)
    print(f"Telah ditangkap jin {nama}...")
    time.sleep(0.5)
    print("Membacakan mantra...")
    time.sleep(0.5)
    print("Jin telah berhasil diubah.")


def isiMatriksUser(file_user_utama,nama_jin,password_jin,role_jin):
    file_user = file_user_utama.matriks
    for i in range(file_user_utama.n_maks):
        if file_user[i][0] == None:
            angka = i
            break
    file_user[angka][0],file_user[angka][1],file_user[angka][2] = nama_jin,password_jin,role_jin


def generateBahan():
    pasir = random.randint(1,5)
    batu = random.randint(1,5)
    air = random.randint(1,5)
    return pasir,batu,air


def ubahBahan(file_bahan_utama,pasir,batu,air):
    file_bahan = file_bahan_utama.matriks
    for i in range(file_bahan_utama.n_maks):
        if file_bahan[i][0] == "pasir":
            bahan = int(file_bahan[i][2])
            file_bahan[i][2] = str(pasir+bahan)
        elif file_bahan[i][0] == "batu":
            bahan = int(file_bahan[i][2])
            file_bahan[i][2] = str(batu+bahan)
        elif file_bahan[i][0] == "air":
            bahan = int(file_bahan[i][2])
            file_bahan[i][2] = str(air+bahan)


def cariSlotCandi(file_candi_utama):
    file_candi = file_candi_utama.matriks
    kosong = True
    for i in range(file_candi_utama.n_maks):
        if file_candi[i][0] == None:
            kosong = False
            return i
    if kosong:
        return None


def hitungJinKumpul(file_user):
    count = 0
    for i in range(102):
        if file_user[i][2] == "jin_pengumpul":
            count += 1
    return count


def hitungJinBangun(file_user):
    count = 0
    for i in range(102):
        if file_user[i][2] == "jin_pembangun":
            count += 1
    return count


def summonjin(file_user_utama):
    file_user = file_user_utama.matriks
    print('Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n (3) Tidak jadi summon jin')
    if cekJumlahJin(file_user):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        while True:
            nomor_jin = int((input("Masukkan nomor jenis jin yang ingin dipanggil: ")))
            if nomor_jin == 1:
                print('Memilih jin "Pengumpul".')
                nama_jin = str(input("Masukkan nama jin: "))
                while cekNamaJin(file_user_utama,nama_jin):
                    print(f"Username “{nama_jin}” sudah diambil!")
                    print("")
                    nama_jin = input("Masukkan nama jin: ")
                password_jin = str(input("Masukkan password jin: "))
                while cekPanjangPassword(password_jin):
                    print("Password panjangnya harus 5-25 karakter!")
                    print("")
                    password_jin = input("Masukkan password jin: ")
                printSummon(nama_jin)
                role_jin = "jin_pengumpul"
                isiMatriksUser(file_user_utama,nama_jin,password_jin,role_jin)
                break
            elif nomor_jin == 2:
                print('Memilih jin "Pembangun".')
                nama_jin = str(input("Masukkan nama jin: "))
                while cekNamaJin(file_user_utama,nama_jin):
                    print(f"Username “{nama_jin}” sudah diambil!")
                    print("")
                    nama_jin = input("Masukkan nama jin: ")
                password_jin = str(input("Masukkan password jin: "))
                while cekPanjangPassword(password_jin):
                    print("Password panjangnya harus 5-25 karakter!")
                    print("")
                    password_jin = input("Masukkan password jin: ")
                printSummon(nama_jin)
                print('Memilih jin "Pembangun".')
                role_jin = "jin_pembangun"
                isiMatriksUser(file_user_utama,nama_jin,password_jin,role_jin)
                break
            elif nomor_jin == 3:
                print("Tidak ada jin yang disummon")
                break
            else:
                print(f'Tidak ada jenis jin bernomor"{nomor_jin}"')


def hapusJin(file_user_utama):
    file_user = file_user_utama.matriks
    nama_jin = input("Masukkan username jin : ")
    if cekNamaJin(file_user,nama_jin):
        Id_jin = getIdJin(file_user,nama_jin)
        command = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
        while not(command == "Y") and not(command == "N"):
            print("Perintah tidak valid, tolong input ulang perintah.")
            command = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
        if command == "Y":
            file_user[Id_jin] = [None,None,None]
            for i in range(Id_jin,(file_user_utama.n_maks-1)):
                file_user[i] = file_user[i+1]
            file_user[file_user_utama.n_maks-1] = [None,None,None]
            printHapus(nama_jin)
        elif command == "N":
            print(f"Jin {nama_jin} tidak jadi dihapus dari alam ghaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")


def ubahTipeJin(file_user_utama):
    file_user = file_user_utama.matriks
    nama_jin = input("Masukkan username jin : ")
    if cekNamaJin(file_user_utama,nama_jin):
        Id_jin = getIdJin(file_user_utama,nama_jin)
        if file_user[Id_jin][2] == "jin_pengumpul":
            command = input(f"Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            while not(command == "Y") and not(command == "N"):
                print("Perintah tidak valid, tolong input ulang perintah.")
                command = input(f"Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            if command == "Y":
                file_user[Id_jin][2] = "jin_pembangun"
                printGanti(nama_jin)
            elif command == "N":
                print(f"Jin pengumpul dengan username {nama_jin} tidak jadi diganti.")
        elif file_user[Id_jin][2] == "jin_pembangun":
            command = input(f"Jin ini bertipe Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            while not(command == "Y") and not(command == "N"):
                print("Perintah tidak valid, tolong input ulang perintah.")
                command = input(f"Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            if command == "Y":
                file_user[Id_jin][2] = "jin_pengumpul"
                printGanti(nama_jin)
            elif command == "N":
                print(f"Jin pembangun dengan username {nama_jin} tidak jadi diganti.")
    else:
        print("Tidak ada jin dengan username tersebut.")


def kumpul(file_bahan_utama, batch):
    file_bahan = file_bahan_utama.matriks
    pasir,batu,air = generateBahan()
    ubahBahan (file_bahan_utama,pasir,batu,air)
    if not(batch):
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")


def bangun(file_bahan_utama,file_candi_utama,jin_pembangun,batch):
    file_bahan = file_bahan_utama.matriks
    file_candi = file_candi_utama.matriks
    pasir,batu,air = generateBahan()
    IdCandi = cariSlotCandi(file_candi_utama)
    if IdCandi != None:
        if int(file_bahan[0][2]) >= pasir and int(file_bahan[1][2]) >= batu and int(file_bahan[2][2]) >= air:
            file_candi[IdCandi][0],file_candi[IdCandi][1],file_candi[IdCandi][2],file_candi[IdCandi][3],file_candi[IdCandi][4] = str(IdCandi),jin_pembangun,str(pasir),str(batu),str(air)
            pasir,batu,air = pasir*-1,batu*-1,air*-1
            ubahBahan(file_bahan,pasir,batu,air)
            if not(batch):
                print("Candi berhasil dibangun !")
            jumlahCandi = 0
            for i in range(file_candi_utama.n_maks):
                if file_candi[i][0] == None:
                    jumlahCandi += 1
            if not(batch):
                print(f"Sisa candi yang perlu dibangun: {jumlahCandi}")
        else:
            if not(batch):
                print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!")
    else:
        if not(batch):
            print("Candi sudah penuh.\nCandi tidak bisa dibangun!")


def batchKumpul(file_bahan_utama, file_user_utama):
    file_user = file_user_utama.matriks
    file_bahan = file_bahan_utama.matriks
    count = hitungJinKumpul(file_user)
    pasir_awal, batu_awal, air_awal = int(file_bahan[0][2]) , int(file_bahan[1][2]), int(file_bahan[2][2])
    if count == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    for i in range(count):
        kumpul(file_bahan_utama,True)
    print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.\nJin menemukan total {-1*pasir_awal + int(file_bahan[0][2])} pasir, {-1*batu_awal+int(file_bahan[1][2])} batu, dan {-1*air_awal+int(file_bahan[2][2])} air.")

def batchBangun(file_bahan_utama, file_user_utama):
    file_user = file_user_utama.matriks
    file_bahan = file_bahan_utama.matriks
    count = hitungJinBangun(file_user)
    #unfinish
    if count == 0:
        print("Bangun candi gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    for i in range(count):
        bangun(file_bahan_utama,True)
    #unfinish
    

def hapusData(matriks_data:MatriksData, data):
    neff = panjang_matriks(matriks_data.matriks, matriks_data.n_maks)
    i_data = getIndeks(matriks_data.matriks, data, matriks_data.n_maks)

    for param in range(matriks_data.n_param):
        matriks_data.matriks[i_data][param] = None

    for data in range(i_data, neff):
        matriks_data.matriks[data] = matriks_data.matriks[data + 1]

    for param in range(matriks_data.n_param):
        matriks_data.matriks[neff][param] = None


def ayamBerkokok(matriks_candi:MatriksData):
    jumlah_candi = panjang_matriks(matriks_candi.matriks, matriks_candi.n_maks)
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


def hancurkanCandi(matriks_candi:MatriksData):
    id = input("Masukkan ID candi: ")
    indeks = getIndeks(matriks_candi.matriks, id, matriks_candi.n_maks)

    if indeks is None:
        print("Tidak ada candi dengan ID tersebut.")
    else:
        opsi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()
        while not (opsi == "Y" or opsi == "N"):
            print("Perintah tidak valid, tolong input ulang perintah.")
            opsi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()

        if opsi == "Y":
            hapusData(matriks_candi, id)
            print("Candi telah berhasil dihancurkan.")
        else:
            print("Understandable, have a nice day.")


def dataJinPembangun(matriks_candi:MatriksData):
    nmaks_jin = 100
    neff_jin = panjang_matriks(matriks_candi.matriks, nmaks_jin)
    matriks_data_pembangun = [[None, None] for i in range(nmaks_jin)]

    for candi in range(neff_jin):
        pembuat = matriks_candi.matriks[candi][1]
        id_pembuat = getIndeks(matriks_data_pembangun, pembuat, nmaks_jin)
        id_kosong = panjang_matriks(matriks_data_pembangun, nmaks_jin)

        if id_pembuat is None:
            matriks_data_pembangun[id_kosong] = [pembuat, 1]
        else:
            matriks_data_pembangun[id_pembuat][1] += 1

    return matriks_data_pembangun


def dataHargaCandi(matriks_candi:MatriksData):
    nmaks_candi = 100
    neff_candi = panjang_matriks(matriks_candi.matriks, nmaks_candi)
    matriks_data_harga = [[None, None] for i in range(nmaks_candi)]

    for candi in range(neff_candi):
        id_candi = matriks_candi.matriks[candi][0]
        pasir = int(matriks_candi.matriks[candi][2])
        batu = int(matriks_candi.matriks[candi][3])
        air = int(matriks_candi.matriks[candi][4])
        harga = pasir*10000 + batu*15000 + air*7500

        matriks_data_harga[candi] = [id_candi, harga]

    return matriks_data_harga


def data_leaderboard(matriks_data):
    nmaks = 100
    neff = panjang_matriks(matriks_data, nmaks)
    matriks_leaderboard = matriks_data

    for i in range(1, neff):
        indeks = i
        while indeks > 0 and matriks_leaderboard[indeks][1] > matriks_leaderboard[indeks - 1][1]:
            temp = matriks_leaderboard[indeks]
            matriks_leaderboard[indeks] = matriks_leaderboard[indeks - 1]
            matriks_leaderboard[indeks - 1] = temp

            indeks -= 1

    return matriks_leaderboard


def laporanJin(matriks_user:MatriksData, matriks_candi:MatriksData, matriks_bahan:MatriksData):
    total_jin, total_pengumpul, total_pembangun = jumlahJin(matriks_user)
    sisa_pasir = matriks_bahan.matriks[0][2]
    sisa_batu = matriks_bahan.matriks[1][2]
    sisa_air = matriks_bahan.matriks[2][2]
    jin_terajin, jin_termalas = "-", "-"

    if total_jin > 0:
        i_maks = 0
        i_min = total_jin - 1

        if data_leaderboard(dataJinPembangun(matriks_candi))[i_maks][0] is not None:
            id_termahal = data_leaderboard(dataJinPembangun(matriks_candi))[i_maks][0]
            harga_termahal = f"({data_leaderboard(dataJinPembangun(matriks_candi))[i_maks][1]})"

        if data_leaderboard(dataJinPembangun(matriks_candi))[i_min][0] is not None:
            id_termurah = data_leaderboard(dataJinPembangun(matriks_candi))[i_min][0]
            harga_termurah = f"({data_leaderboard(dataJinPembangun(matriks_candi))[i_min][1]})"

    print(f"""
> Total Jin: {total_jin}
> Total Jin Pengumpul: {total_pengumpul}
> Total Jin Pembangun: {total_pembangun}
> Jin Terajin: {jin_terajin}
> Jin Termalas: {jin_termalas}
> Jumlah Pasir Tersisa: {sisa_pasir} unit
> Jumlah Air Tersisa: {sisa_air} unit
> Jumlah Batu Tersisa: {sisa_batu} unit
""")


def laporanCandi(matriks_candi:MatriksData):
    total_candi = panjang_matriks(matriks_candi.matriks, matriks_candi.n_maks)
    total_pasir, total_batu, total_air = jumlahBahan(matriks_candi)
    id_termahal, id_termurah = "-", "-"
    harga_termahal, harga_termurah = "", ""

    if total_candi > 0:
        i_maks = 0
        i_min = total_candi - 1

        if data_leaderboard(dataHargaCandi(matriks_candi))[i_maks][0] is not None:
            id_termahal = data_leaderboard(dataHargaCandi(matriks_candi))[i_maks][0]
            harga_termahal = f"({data_leaderboard(dataHargaCandi(matriks_candi))[i_maks][1]})"

        if data_leaderboard(dataHargaCandi(matriks_candi))[i_min][0] is not None:
            id_termurah = data_leaderboard(dataHargaCandi(matriks_candi))[i_min][0]
            harga_termurah = f"({data_leaderboard(dataHargaCandi(matriks_candi))[i_min][1]})"
        
    print(f"""
> Total Candi: {total_candi}
> Total Pasir yang Digunakan: {total_pasir}
> Total Air yang Digunakan: {total_air}
> Total Batu yang Digunakan: {total_batu}
> ID Candi Termahal: {id_termahal} {harga_termahal}
> ID Candi Termurah: {id_termurah} {harga_termurah}
""")


def printLeaderboard(matriks_leaderboard):
    nmaks = 100
    neff = panjang_matriks(matriks_leaderboard, nmaks)

    for data in range(neff):
        print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")