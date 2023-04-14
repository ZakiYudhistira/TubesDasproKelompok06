import argparse, os, time, Module

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

nama_folder = args.nama_folder
parent_folder = "save"
save_directory = f"{parent_folder}\\{nama_folder}"

if os.path.exists(save_directory):
    
    Module.dotdotdot("Loading", 3, 0.5)

    matriks_user = Module.MatriksData(f"{save_directory}\\user.csv", "user", 3, 102)
    matriks_candi = Module.MatriksData(f"{save_directory}\\candi.csv", "candi", 5, 100)
    matriks_bahan = Module.MatriksData(f"{save_directory}\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
    tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
    
    print("Selamat datang di program \"Manajerial Candi\"")

    program_jalan = True
    logged_in = False
    logged_in_as = ""

    while program_jalan:
        command = str(input(">>> "))
        if command == "login":
            if logged_in:
                print("Login gagal! Anda telah login dengan username "+user+", silahkan lakukan “logout” sebelum melakukan login kembali.")
            else:
                logged_in,user,logged_in_as = Module.login(matriks_user.matriks)

        elif command == "logout":
            if logged_in:
                print("Terimakasih "+user+"! sampai jumpa di lain waktu")
                logged_in,user,logged_in_as = Module.logout()
            else:
                print("Logout gagal!"+'\n'+"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        
        elif command == "exit":
            if logged_in:
                print("Mohon logout dulu sebelum keluar dari program")
            else:
                while True:
                    opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").upper()
                    if opsi == "Y":
                        tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
                        Module.save_data(tuple_matriks_data)
                        time.sleep(0.5)
                        print("Terima kasih sudah menjalankan program!")
                        break
                    elif opsi == "N":
                        break
                program_jalan = False
        
        elif command == "save":
            tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
            Module.save_data(tuple_matriks_data)
        
        else:
            print("Perintah tidak dikenali")
            
else:
    print(f"Folder \"{nama_folder}\" tidak ditemukan.")