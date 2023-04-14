import time
import Module
def cekNamaJin(file_user,nama_jin):
    for i in range(len(file_user)):
        if nama_jin == file_user[i][0]:
            return True
    return False

def getIdJin(file_user,nama_jin):
    for i in range(len(file_user)):
        if nama_jin == file_user[i][0]:
            return i

def cekPanjangPassword (password):
    char = 0
    for i in password:
        char+=1
    if char < 5 or char > 25:
        return True
    else:
        return False

def cekJumlahJin(file_user):
    if type(file_user[101][0]) == None:
        return True
    else:
        return False

def printSummon(nama):
    print("Mengumpulkan sesajen...")
    time.sleep(0.5)
    print("Menyerahkan sesajen...")
    time.sleep(0.5)
    print("Membacakan mantra...")
    time.sleep(0.5)
    print(f"Jin {nama} berhasil dipanggil!")

def printHapus(nama):
    print(f"Dicari jin {nama}...")
    time.sleep(0.5)
    print(f"Telah ditangkap jin {nama}...")
    time.sleep(0.5)
    print("Membacakan mantra...")
    time.sleep(0.5)
    print("Jin telah berhasil dihapus dari alam gaib.")

def printGanti(nama):
    print(f"Dicari jin {nama}...")
    time.sleep(0.5)
    print(f"Telah ditangkap jin {nama}...")
    time.sleep(0.5)
    print("Membacakan mantra...")
    time.sleep(0.5)
    print("Jin telah berhasil diubah.")

def isiMatriksUser(file_user,nama_jin,password_jin,role_jin):
    for i in range(len(file_user)):
        if file_user[i][0] == None:
            angka = i
            break
    file_user[angka][0],file_user[angka][1],file_user[angka][2] = nama_jin,password_jin,role_jin

def summonjin(file_user):
    print('Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n (3) Tidak jadi summon jin')
    if cekJumlahJin(file_user):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        while True:
            nomor_jin = int((input("Masukkan nomor jenis jin yang ingin dipanggil: ")))
            if nomor_jin == 1:
                print('Memilih jin "Pengumpul".')
                nama_jin = str(input("Masukkan nama jin: "))
                while cekNamaJin(file_user,nama_jin):
                    print(f"Username “{nama_jin}” sudah diambil!")
                    print("")
                    nama_jin = input("Masukkan nama jin: ")
                password_jin = str(input("Masukkan password jin: "))
                while cekPanjangPassword(password_jin):
                    print("Password panjangnya harus 5-25 karakter!")
                    print("")
                    password_jin = input("Masukkan password jin: ")
                printSummon(nama_jin)
                role_jin = "jin_pengumpul"
                isiMatriksUser(file_user,nama_jin,password_jin,role_jin)
                break
            elif nomor_jin == 2:
                print('Memilih jin "Pengumpul".')
                nama_jin = str(input("Masukkan nama jin: "))
                while cekNamaJin(file_user,nama_jin):
                    print(f"Username “{nama_jin}” sudah diambil!")
                    print("")
                    nama_jin = input("Masukkan nama jin: ")
                password_jin = str(input("Masukkan password jin: "))
                while cekPanjangPassword(password_jin):
                    print("Password panjangnya harus 5-25 karakter!")
                    print("")
                    password_jin = input("Masukkan password jin: ")
                printSummon(nama_jin)
                print('Memilih jin "Pembangun".')
                role_jin = "jin_pembangun"
                isiMatriksUser(file_user,nama_jin,password_jin,role_jin)
                break
            elif nomor_jin == 3:
                print("Tidak ada jin yang disummon")
                break
            else:
                print(f'Tidak ada jenis jin bernomor"{nomor_jin}"')

def hapusJin(file_user):
    nama_jin = input("Masukkan username jin : ")
    if cekNamaJin(file_user,nama_jin):
        Id_jin = getIdJin(file_user,nama_jin)
        command = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
        while not(command == "Y") and not(command == "N"):
            print("Perintah tidak valid, tolong input ulang perintah.")
            command = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
        if command == "Y":
            file_user[Id_jin] = [None,None,None]
            file_user[len(file_user)-1] = [None,None,None]
            for i in range(Id_jin,(len(file_user)-1)):
                file_user[i] = file_user[i+1]
            printHapus(nama_jin)
        elif command == "N":
            print(f"Jin {nama_jin} tidak jadi dihapus dari alam ghaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")

def ubahTipeJin(file_user):
    nama_jin = input("Masukkan username jin : ")
    if cekNamaJin(file_user,nama_jin):
        Id_jin = getIdJin(file_user,nama_jin)
        if file_user[Id_jin][2] == "jin_pengumpul":
            command = input(f"Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            while not(command == "Y") and not(command == "N"):
                print("Perintah tidak valid, tolong input ulang perintah.")
                command = input(f"Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            if command == "Y":
                file_user[Id_jin][2] = "jin_pembangun"
                printGanti(nama_jin)
            elif command == "N":
                print(f"Jin pengumpul dengan username {nama_jin} tidak jadi diganti.")
        elif file_user[Id_jin][2] == "jin_pembangun":
            command = input(f"Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            while not(command == "Y") and not(command == "N"):
                print("Perintah tidak valid, tolong input ulang perintah.")
                command = input(f"Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            if command == "Y":
                file_user[Id_jin][2] = "jin_pengumpul"
                printGanti(nama_jin)
            elif command == "N":
                print(f"Jin pembangun dengan username {nama_jin} tidak jadi diganti.")
    else:
        print("Tidak ada jin dengan username tersebut.")

file_utama = Module.load_data("user.csv", 3 ,102)
# summonjin(file_utama)
# summonjin(file_utama)
# hapusJin(file_utama)
ubahTipeJin(file_utama)
print(file_utama)