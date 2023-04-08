import csv
data_user_read = open('user.csv','r')
data_user_reader = csv.reader(data_user_read,delimiter=';')

def login():
    akses = False
    while akses == False:
        user = input("Masukkan username : ")
        password = input("Masukkan password : ")
        for row in data_user_reader:
            cek_user = (row[0],row[1])
            if cek_user == (user,password):
                akses = True
        if akses == False:
            print("Username dan password tidak sesuai atau username tidak terdaftar, mohon coba lagi")
        else :
            print("Login berhasil")
login()