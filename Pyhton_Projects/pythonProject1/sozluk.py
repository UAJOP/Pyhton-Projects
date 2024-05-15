musteri = {"ad":"kaan",
           "soyad":"balcı",
           "yas":22}
print(musteri["ad"])
musteri["yas"]=23
print(musteri.pop("yas"))
print(musteri)
print(musteri.values())
print(musteri.keys())
print(musteri.items())

for anahtar,deger in musteri.items():
    print(f"{anahtar},{deger}")

ogrenci = {"derya":[50,75,90],
           "mesut":[42,65,78],
           "kaan":[13,55,78]
}

print(ogrenci["mesut"][0])
print(ogrenci["mesut"][2])
liste= ogrenci["mesut"]

ogrenci["mesut"].append(52)
print(ogrenci)
