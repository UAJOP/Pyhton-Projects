def toplam():
    sayı1=54
    sayı2=45
    toplam = sayı1+sayı2
    print("Toplam değer",toplam)
    toplam()

def toplam2(sayı1,sayı2):
        toplam = sayı1+sayı2
        print(f"{sayı1} ve {sayı2} toplamı {toplam}")

toplam2(45,65)
toplam2(89,86)


def toplam3(sayı1,sayı2):
    toplam = sayı1+sayı2
    return toplam

print(toplam3(65,35))
denklem = toplam3(32,45)-15
print(denklem)


