musteri = {"ad":"Burak",
           "soyad":"Evren",
           "yas":35,
           "email":"burak@brk.com"}

print("Müşteri Adı:", musteri["ad"])
musteri["yas"]=40
print("Müşteri Yaşı",musteri["yas"])
musteri.pop("yas")
print(musteri)

print(musteri.values())
print(musteri.keys())
print(musteri.items())

for anahtar,deger in musteri.items():
    print(f"{anahtar}:{deger}")



