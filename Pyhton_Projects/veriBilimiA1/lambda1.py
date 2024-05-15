def kareAl(sayi):
    sonuc = sayi ** 2
    return sonuc


print("Birinci Fonksiyon", kareAl(5))


def toplam(sayi1, sayi2):
    return sayi1 + sayi2


print(toplam(54, 56))


# lambdaWay

kareAl2 = lambda sayi: sayi ** 2

print("2. fonk", kareAl2(5))


toplam2 = lambda sayi3, sayi4: sayi3 + sayi4


print("toplam2", toplam2(54, 56))
