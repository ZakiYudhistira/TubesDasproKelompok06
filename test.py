import argparse, os, time
from Module import *

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

nama_folder = args.nama_folder
parent_folder = "save"
save_directory = f"{parent_folder}\\{nama_folder}"

dotdotdot("Loading", 3, 0.5)

matriks_user = MatriksData(f"{save_directory}\\user.csv", "user", 3, 102)
matriks_candi = MatriksData(f"{save_directory}\\candi.csv", "candi", 5, 100)
matriks_bahan = MatriksData(f"{save_directory}\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

print("Selamat datang di program \"Manajerial Candi\"!")
print("Ketik help untuk menampilkan command.")

program_jalan = True
logged_in = False
logged_in_as = ""
user = ""

matriks_leaderboard = dataJinPembangun(matriks_user, matriks_candi, "total_bahan")
print(dataLeaderboard(matriks_user, matriks_candi, matriks_leaderboard, "jin"))