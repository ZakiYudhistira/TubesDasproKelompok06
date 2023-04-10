import argparse, os, Module

#parser = argparse.ArgumentParser()
#parser.add_argument("nama_folder", help="folder data yang ingin di-load")
#args = parser.parse_args()

filepath = os.path.dirname(os.path.realpath(__file__))
#folder = args.nama_folder
#save_folderpath = f"{filepath}\\{folder}"

class MatriksData:
    def __init__(self, nama_file, nama_data, n_param, n_max, matriks = None):
        self.nama_file = nama_file
        self.matriks = Module.load_data(nama_file, n_param, n_max)
        self.n_param = n_param
        self.n_max = n_max
        self.nama_data = nama_data


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

def panjang_matriks(matriks_data):
    count = 0
    for baris in range(matriks_data.n_max):
        if matriks_data.matriks[baris][0] is not None:
            count += 1
        else:
            break
        
    return count

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

