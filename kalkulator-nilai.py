print("===== KALKULATOR PENILAIAN =====")

nilai = float(input("Masukkan nilai[0-100]: "))

if nilai >= 85:
    print('Lulus dengan perdikat : A')
elif nilai >= 70:
    print('Lulus dengan predikat : B')
elif nilai >= 60:
    print('Lulus dengan predikat : C')
elif nilai >= 50:
    print('Tidak lulus dengan predikat : D')
else:
    print('Mengulang dengan predikat : E')