ogrenciler = ["Baran","Efe","Joker","Allame"]
def ogrencileriAyir(ogrenciListesi):
    grup = [[]] , [[]]
    for i,item in enumerate(ogrenciListesi):
        if i %2==0:
            grup[0].append(item)
        else:
            grup[1].append(item)
    return grup
liste = ogrencileriAyir(ogrenciler)
print(liste)