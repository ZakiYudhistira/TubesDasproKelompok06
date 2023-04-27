import argparse, os
from Module import *

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

nama_folder = args.nama_folder
parent_folder = "save"
save_directory = f"{parent_folder}\\{nama_folder}"

if os.path.exists(save_directory):
    
    dotdotdot("Loading", 3, 0.5)

    matriks_user = MatriksData(f"{save_directory}\\user.csv", "user", 3, 102)
    matriks_candi = MatriksData(f"{save_directory}\\candi.csv", "candi", 5, 100)
    matriks_bahan = MatriksData(f"{save_directory}\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
    tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

    print(matriks_candi.matriks[:panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)])
    print(matriks_bahan.matriks)
    bangun(matriks_bahan, matriks_candi, "setan", 3, 4, 5, False)
    print(matriks_bahan.matriks)
    print(matriks_candi.matriks[:panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)])

else:
    print(f"Folder \"{nama_folder}\" tidak ditemukan.")