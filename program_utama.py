import argparse, os, time
from subprogram import *

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
    
    print("Selamat datang di program “Manajerial Candi”!")
    print("Ketik help untuk menampilkan command.")

    program_jalan = True
    logged_in = False
    logged_in_as = ""
    user = ""

    while program_jalan:
        command = input(">>> ").lower()
        if command == "login":
            if logged_in:
                print(f"Login gagal! Anda telah login dengan username {user}, silakan lakukan “logout” sebelum melakukan login kembali.")
            else:
                logged_in,user,logged_in_as = login(matriks_user)

        elif command == "logout":
            if logged_in:
                print(f"Terimakasih {user}! Sampai jumpa di lain waktu")
                logged_in,user,logged_in_as = logout()
            else:
                print("Logout gagal!\nAnda belum login, silakan login terlebih dahulu sebelum melakukan logout.")
        
        elif command == "help":
            if logged_in:
                help(logged_in_as)
            else:
                print("""Berikut merupakan beberapa command yang bisa Anda lakukan:
1.login: Untuk masuk menggunakan akun.
2.save: Untuk menyimpan hasil permainan.
3.exit: Untuk keluar dari program.""")

        elif command == "save":
            tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
            saveData(tuple_matriks_data)
        
        elif command == "bangun":
            if logged_in_as == "jin_pembangun":
                pasir, batu, air = generateBahan()
                bangun(matriks_bahan, matriks_candi, user, pasir, batu, air)
            else:
                print("User bukan jin pembangun\nPembangunan candi tidak dilakukan.")

        elif command == "kumpul":
            if logged_in_as == "jin_pengumpul":
                kumpul(matriks_bahan,False)
            else:
                print("User bukan jin pengumpul\nPengumpulan bahan tidak dilakukan.")
        
        elif command == "showbahan":
            if logged_in_as == "bandung_bondowoso":
                showBahan(matriks_bahan)
            else:
                print("User bukan Bandung Bondowoso\nTidak bisa mengecek jumlah bahan yang tersedia.")

        elif command == "hapusjin":
            if logged_in_as == "bandung_bondowoso":
                hapusJin(matriks_user, matriks_candi)
            else:
                print("User bukan Bandung Bondowoso\nPengubahan jin tidak dilakukan.")

        elif command == "ubahjin":
            if logged_in_as == "bandung_bondowoso":
                ubahTipeJin(matriks_user)
            else:
                print("User bukan Bandung Bondowoso\nPengubahan jin tidak dilakukan.")
        
        elif command == "summonjin":
            if logged_in_as == "bandung_bondowoso":
                summonJin(matriks_user)
            else:
                print("User bukan Bandung Bondowoso\nSummon jin tidak dilakukan.")
        
        elif command == "batchkumpul":
            if logged_in_as == "bandung_bondowoso":
                batchKumpul(matriks_bahan,matriks_user)
            else:
                print("User bukan Bandung Bondowoso\nBatch kumpul bahan tidak dilakukan.")

        elif command == "batchbangun":
            if logged_in_as == "bandung_bondowoso":
                batchBangun(matriks_bahan,matriks_candi,matriks_user)
            else:
                print("User bukan Bandung Bondowoso\nBatch bangun bahan tidak dilakukan.")

        elif command == "laporanjin":
            if logged_in_as == "bandung_bondowoso":
                laporanJin(matriks_user, matriks_candi, matriks_bahan)   
            else:
                print("User bukan Bandung Bondowoso\nTidak bisa mengambil laporan jin!")

        elif command == "laporancandi":
            if logged_in_as == "bandung_bondowoso":
                laporanCandi(matriks_user, matriks_candi, matriks_bahan)
            else:
                print("User bukan Bandung Bondowoso\nTidak bisa mengambil laporan candi!")

        elif command == "leaderboard":
            if logged_in_as == "bandung_bondowoso":
                printLeaderboard(matriks_user, matriks_candi)
            else:
                print("User bukan Bandung Bondowoso\nTidak bisa melihat leaderboard!")

        elif command == "hancurkancandi":
            if logged_in_as == "roro_jonggrang":
                hancurkanCandi(matriks_candi)
            else:
                print("User bukan Roro Jonggrang\nTidak boleh menghancurkan candi orang!")

        elif command == "ayamberkokok":
            if logged_in_as == "roro_jonggrang":
                ayamBerkokok(matriks_candi)
            else:
                print("User bukan Roro Jonggrang\nAyam tidak mau berkokok!")
                
        elif command == "exit":
            if logged_in:
                print("Mohon logout dulu sebelum keluar dari program.")
            else:
                opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ").upper()
                while not(opsi == "Y" or opsi == "N"):
                    print("Perintah tidak valid, tolong input ulang perintah.")
                    opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ").upper()

                if opsi == "Y":
                    tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
                    saveData(tuple_matriks_data)
                    time.sleep(0.5)
                    print("Terima kasih sudah menjalankan program!")
                    time.sleep(0.5)
                else:
                    print("Baik.")
                    time.sleep(0.5)
                    print("Terima kasih sudah menjalankan program!")
                    time.sleep(0.5)

                program_jalan = False

        else:
            print("Perintah tidak dikenali")
            
else:
    print(f"Folder “{nama_folder}” tidak ditemukan.")