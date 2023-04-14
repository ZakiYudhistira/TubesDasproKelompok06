# Library fungsi - fungsi program
import os, time, random

filepath = os.path.dirname(os.path.realpath(__file__))

class MatriksData:
    def __init__(self, nama_file, nama_data, n_param, n_max, matriks = None):
        self.nama_file = nama_file
        self.nama_data = nama_data
        self.n_param = n_param
        self.n_max = n_max
        self.matriks = load_data(nama_file, n_param, n_max)


#-------------------------------------------------Fungsi save_file-----------------------------------------------------------
# Procedure mengoutput teks dengan dot dot dot yang dramatis.
def dotdotdot(teks, n_dot, interval):
    print(teks, end="", flush=True)
    time.sleep(interval)
    for i in range(n_dot):
        print('.', end="", flush=True)
        time.sleep(interval)
    print()


#-------------------------------------------------Fungsi save_file-----------------------------------------------------------
# Procedure untuk menyimpan file berdasarkan path dan data yang diberikan .
def save_file(path, data):
    with open(path, 'w') as file:
        file.write(data)

#-------------------------------------------------Fungsi login-----------------------------------------------------------
# Fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil
def login(matriks_data_user):
    data_user = matriks_data_user
    akses = False
    username = True
    password_p = True
    user = input("Masukkan username : ")
    password = input("Masukkan password : ")
    
    for i in range(102): # loop pemrosesan file csv untuk menentukan password dan username
        if data_user[i][0] == user:
            if data_user[i][1] == password:
                akses = True
                break
            else:
                akses = False
                password_p = False
        else:
            akses = False

    if akses:
        print("Selamat Datang, "+user+"!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return akses,data_user[i][0],data_user[i][2]
    else :
        if username and not(password_p):
            print("Password salah!")
        elif not(username):
            print("Username tidak terdaftar!")
        return akses," ", " "

#-------------------------------------------------Fungsi logout-----------------------------------------------------------
def logout():
    return False, " ", " "



#-------------------------------------------------Fungsi load_data-----------------------------------------------------------
# Mengembalikan sebuah martriks berisi data yang dibaca dengan jumlah baris n_max dan jumlah kolom n_param.
def load_data(nama_file, n_param, n_max):

    with open(nama_file, 'r') as file:
        data_file = file.read()
        matriks_data = [[None for i in range(n_param)] for j in range(n_max)]
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


#-------------------------------------------------Fungsi panjang_matriks-----------------------------------------------------------
# Mengembalikan panjang matriks_data yang terisi.
def panjang_matriks(matriks_data):
    count = 0
    for baris in range(matriks_data.n_max):
        if matriks_data.matriks[baris][0] is not None:
            count += 1
        else:
            break
        
    return count

#-------------------------------------------------Fungsi tulis_matriks_data-----------------------------------------------------------
# Mengembalikan string berisi data setiap MatriksData dengan format yang sama dengan isi file eksternal.
def tulis_matriks_data(matriks_data):
    if matriks_data.nama_data == "user":
        string_data = "username;password;role"
    elif matriks_data.nama_data == "candi":
        string_data = "id;pembuat;pasir;batu;air"
    elif matriks_data.nama_data == "bahan_bangunan":
        string_data = "nama;deskripsi;jumlah"

    if panjang_matriks(matriks_data) != 0:
        string_data += '\n'

    for baris in range(panjang_matriks(matriks_data)):
        for param in range(matriks_data.n_param):
            if param != (matriks_data.n_param - 1):
                string_data = string_data + matriks_data.matriks[baris][param] + ';'
            else:
                if baris != (panjang_matriks(matriks_data) - 1):
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


