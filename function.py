# jawaban no.1
def profile(nama,alamat,gender,umur):
    print("nama saya",nama)
    print("alamat domisili saya di",alamat)
    print("dengan jenis kelamin",gender)
    print("dan berusia",umur)
# panggil
profile("Amanda Fiqih Hauli", "Depok", "perempuan", "20 tahun")


# jawaban no.2
def kelulusan(nilai):
    
    if nilai <= 60:
        return f"{nilai} adalah Gagal"
    elif nilai <= 70:
        return f"{nilai} adalah Baik."
    elif nilai <= 80:
        return f"{nilai} adalah Sangat Baik"
    elif nilai <= 100:
        return f"{nilai} adalah Istimewa"
    else:
        return f"{nilai} salah input"
# panggil
nilai = int(input("masukan nilai = "))
hasil = kelulusan(nilai)
print("hasil nilai kelulusan",hasil)


# jawaban no.3
def number(x):
    for i in range (1, x+1, 2):
        print(i)
# panggil
number(100)
    
    
