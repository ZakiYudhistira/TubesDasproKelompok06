import csv # melakukan import library
data_user_read = open('user.csv','r') #inisialisasi read file csv
data_user_reader = csv.reader(data_user_read,delimiter=';')
#------------------------------------------------------------------------------------------------------------ Fungsi login
def login(): # fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil
    data_user_read = open('user.csv','r') #inisialisasi read file csv
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