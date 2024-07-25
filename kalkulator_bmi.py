#Program Perhitungan BMI

print ("PERHITUNGAN BMI (BODY MASS INDEX)")
print("----------------------------------")

berat_badan = input("Masukkan Berat Badan Anda (Kilogram): ") # ini hasilnya string
berat_badan = float(berat_badan) #konversi dari string ke float
tinggi_badan = input("Masukkan Tinggi Badan Anda (Meter): ") # ini hasilnya string
tinggi_badan = float(tinggi_badan) #konversi dari string ke float

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

# print(berat_badan_ideal)

print(f"Nilai BMI Anda Adalah {bmi:.2f} kg/m^2")
print("Nilai BMI normal anda adalah 18.5 kg/m^2 - 25 kg/m^2")
print(f"Berat Badan Ideal Anda Adalah Dalam Rentang "
      f"{berat_badan_ideal['bawah']:.2f}KG - {berat_badan_ideal['atas']:.2f}KG")

print("---------------------------------------------")
print("Terima Kasih Sudah Menggunakan Program Ini :3")