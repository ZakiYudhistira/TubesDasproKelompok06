import argparse, os, Module, csv

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

filepath = os.path.dirname(os.path.realpath(__file__))
folder_save = args.nama_folder

class MatriksData:
    def __init__(self, file, n_param, n_max, matriks = None):
        self.file = file
        self.n_param = n_param
        self.n_max = n_max
        self.matriks = Module.load_data(file, n_param, n_max)

data_user_read = open(f"{filepath}\\save\\user.csv",'r') #inisialisasi read file csv
data_user_reader = csv.reader(data_user_read,delimiter=';')
#------------------------------------------------------------------------------------------------------------ Fungsi login
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

#------------------------------------------------------------------------------------------------------------ Fungsi logout    
def logout():
    return False, " ", " "



#------------------------------------------------------------------------------------------------------------ Fungsi load_data
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
