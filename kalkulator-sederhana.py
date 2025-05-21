print("===== KALKULATOR SEDERHANA =====")

inputanPertama = int(input("Masukkan angka: "))
inputanKedua = int(input("Masukkan angka: "))

print("Pilihlah operasi yang anda inginkan!")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Modulus")

inputOperasi = int(input("Masukkan pilihan: "))

penjumlahan = inputanPertama + inputanKedua
pengurangan = inputanPertama - inputanKedua
perkalian = inputanPertama * inputanKedua
pembagian = inputanPertama / inputanKedua
modulus = inputanPertama % inputanKedua

if inputOperasi == 1 :
    print("Hasil Penjumlahan: ", penjumlahan)
elif inputOperasi == 2 :
    print("Hasil Pengurangan: ",pengurangan)
elif inputOperasi == 3 :
    print("Hasil Perkalian: ",perkalian)
elif inputOperasi == 4 : 
    print("Hasil Pembagian: ",pembagian)
elif inputOperasi == 5 : 
    print("Hasil Modulus: ",modulus)