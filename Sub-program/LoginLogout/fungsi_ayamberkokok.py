def load_data(filename):
    file = open(filename, 'r').read()
    if filename == "user.csv":
        NMax = 102
        NParam = 3
    elif filename == "candi.csv":
        NMax = 100
        NParam = 5
    else:
        NMax = 4
        NParam = 3

    matriks_data = [[0 for i in range(NParam)] for j in range(NMax)]
    data = ''
    indeks_baris = 0
    indeks_kolom = 0

    for huruf in file:
        if huruf == ';' or huruf == '\n':
            if huruf != '\n':
                matriks_data[indeks_baris][indeks_kolom] = data
                indeks_kolom += 1
            else:
                matriks_data[indeks_baris][indeks_kolom] = data
                indeks_baris += 1
                indeks_kolom = 0
            data = ''
        else:
            data += huruf

    if data != '':
        matriks_data[indeks_baris][indeks_kolom] = data

    return matriks_data


