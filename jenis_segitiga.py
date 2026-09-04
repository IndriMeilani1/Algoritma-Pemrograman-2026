print("PROGRAM MENENTUKAN JENIS SEGITIGA")
print("----------------------------------")

a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Hasil: Bukan segitiga")

elif a == b and b == c:
    print("Hasil: Segitiga sama sisi")

elif a == b or a == c or b == c:
    print("Hasil: Segitiga sama kaki")

else:
    print("Hasil: Segitiga sembarang")