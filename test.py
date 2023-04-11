import argparse, os, time, Module

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

folder_data = args.nama_folder

if os.path.exists(folder_data):

    Module.dotdotdot("Loading", 3, 0.5)

    matriks_user = Module.MatriksData(f"{folder_data}\\user.csv", "user", 3, 102)
    matriks_candi = Module.MatriksData(f"{folder_data}\\candi.csv", "candi", 5, 100)
    matriks_bahan = Module.MatriksData(f"{folder_data}\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
    tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

    print("Selamat datang di program \"Manajerial Candi\"")

    Module.save_data(tuple_matriks_data)
else:
    print(f"Folder \"{folder_data}\" tidak ditemukan.")
