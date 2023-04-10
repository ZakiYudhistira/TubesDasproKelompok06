import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="folder data yang ingin di-load")
args = parser.parse_args()

filepath = os.path.dirname(os.path.realpath(__file__))
folder = args.nama_folder
pathfolder_save = f"{filepath}\\{folder}"

class MatriksData:
    def __init__(self, nama_file, n_param, n_max, matriks = None):
        self.nama_file = nama_file
        self.n_param = n_param
        self.n_max = n_max
        self.matriks = load_data(nama_file, n_param, n_max)

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
