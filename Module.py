import argparse, os, csv

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

filepath = os.path.dirname(os.path.realpath(__file__))
folder_save = args.nama_folder

data_user_read = open(f"{filepath}\\save\\user.csv",'r') #inisialisasi read file csv
data_user_reader = csv.reader(data_user_read,delimiter=';')

class MatriksData:
    def __init__(self, nama_file, nama_data, n_param, n_max, matriks = None):
        self.nama_file = nama_file
        self.nama_data = nama_data
        self.n_param = n_param
        self.n_max = n_max
        self.matriks = load_data(nama_file, n_param, n_max)


#-------------------------------------------------Fungsi login-----------------------------------------------------------
def login(): # fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil
    data_user_read = open(f"{filepath}\\save\\user.csv",'r') #inisialisasi read file csv
    data_user_reader = csv.reader(data_user_read,delimiter=';')
    akses = False
    username = True
    password_p = True
    user = input("Masukkan username : ")
    password = input("Masukkan password : ")
    for row in data_user_reader: # loop pemrosesan file csv untuk menentukan password dan username
        cek_user = (row[0],row[1])
        logged_in_as = row[2]
        if cek_user == (user,password):
            akses = True
        elif user == row[0] and password != row[1]:
            username = True
            password_p = False
        elif user != row[0]:
            username = False
    if akses:
        print("Selamat Datang, "+user+"!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return akses, user, logged_in_as
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
def load_data(nama_file, n_param, n_max):
    file = open(nama_file, 'r').read()

    matriks_data = [[None for i in range(n_param)] for j in range(n_max)]
    data = ''
    indeks_baris = 0
    indeks_kolom = 0

    for huruf in file:
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

    if data != '':
        matriks_data[indeks_baris-1][indeks_kolom] = data

    return matriks_data


#-------------------------------------------------Fungsi tulis_data_matriks-----------------------------------------------------------
# Mengembalikan panjang matriks_data yang terisi.
def panjang_matriks(matriks_data):
    count = 0
    for baris in range(matriks_data.n_max):
        if matriks_data.matriks[baris][0] is not None:
            count += 1
        else:
            break
        
    return count

#-------------------------------------------------Fungsi tulis_data_matriks-----------------------------------------------------------
# Mengembalikan string berisi data setiap MatriksData dengan format yang sama dengan isi file eksternal.
def tulis_data_matriks(matriks_data):
    if matriks_data.nama_data == "user":
        string_data = "username;password;role\n"
    elif matriks_data.nama_data == "candi":
        string_data = "id;pembuat;pasir;batu;air\n"
    elif matriks_data.nama_data == "bahan_bangunan":
        string_data = "nama;deskripsi;jumlah\n"

    for baris in range(panjang_matriks(matriks_data)):
        for param in range(matriks_data.n_param):
            if param != (matriks_data.n_param - 1):
                string_data = string_data + matriks_data.matriks[baris][param] + ';'
            else:
                string_data = string_data + matriks_data.matriks[baris][param] + '\n'

    return string_data
