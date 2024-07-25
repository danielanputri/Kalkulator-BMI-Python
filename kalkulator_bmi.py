#Program Perhitungan BMI

print ("PERHITUNGAN BMI (BODY MASS INDEX)")
print("----------------------------------")

berat_badan = float(input("Masukkan Berat Badan Anda (Kilogram): ")) # ini hasilnya string, lebih ringkas koversinya kalau begini
# berat_badan = float(berat_badan) #konversi dari string ke float
tinggi_badan = float(input("Masukkan Tinggi Badan Anda (Meter): ")) # ini hasilnya string, lebih ringkas koversinya kalau begini
# tinggi_badan = float(tinggi_badan) #konversi dari string ke float

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

if bmi < 18.5:
    kategori = ('Anda Kekurangan Berat Badan')
elif bmi < 25:
    kategori = ('Nilai BMI Anda Normal')
elif bmi < 30:
    kategori = ('Anda Kelebihan Berat Badan')
else:
    kategori = ('Anda Mengalami Obesitas')

print(f"\nNilai BMI Anda Adalah {bmi:.2f} kg/m^2")
print(kategori)
print(f"Berat Badan Ideal Anda Adalah Dalam Rentang "
      f"{berat_badan_ideal['bawah']:.2f}KG - {berat_badan_ideal['atas']:.2f}KG")

print("\n---------------------------------------------")
print("Terima Kasih Sudah Menggunakan Program Ini :3")