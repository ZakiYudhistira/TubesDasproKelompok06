import time
import Module
def cekNamaJin(file_user,nama_jin):
    for i in range(len(file_user)):
        if nama_jin == file_user[i][0]:
            return True
    return False

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

def isiMatriksUser(file_user,nama_jin,password_jin,role_jin):
    for i in range(len(file_user)):
        if file_user[i][0] == None:
            angka = i
            break
    file_user[angka][0],file_user[angka][1],file_user[angka][2] = nama_jin,password_jin,role_jin

def summonjin(file_user):
    print('Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n')
    if cekJumlahJin(file_user):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        while True:
            nomor_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
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
                    nama_jin = input("Masukkan password jin: ")
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
                    nama_jin = input("Masukkan password jin: ")
                printSummon(nama_jin)
                print('Memilih jin "Pembangun".')
                role_jin = "jin_pembangun"
                isiMatriksUser(file_user,nama_jin,password_jin,role_jin)
                break
            else:
                print(f'Tidak ada jenis jin bernomor"{nomor_jin}"')

file_utama = Module.load_data("user.csv", 3 ,102)
summonjin(file_utama)
summonjin(file_utama)
print(file_utama)