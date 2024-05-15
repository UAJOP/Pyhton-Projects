sifir = int(input("0 verenler sayısı"))
bir = int(input("1 verenler sayısı"))
iki = int(input("2 verenler sayısı"))
üc = int(input("3 verenler sayısı"))
dört = int(input("4 verenler sayısı"))
beş = int(input("5 verenler sayısı"))
altı = int(input("6 verenler sayısı"))

yedi = int(input("7 verenler sayısı"))
sekiz = int(input("8 verenler sayısı"))

dokuz = int(input("9 verenler sayısı"))
on = int(input("10 verenler sayısı"))

kötüleyen = sifir+bir+iki+üc+dört+beş+altı

nötr = yedi+sekiz

destekleyenler = dokuz+on

toplam = kötüleyen+nötr+destekleyenler

desteyelenYüzdesi = (destekleyenler/toplam)*100
kotuleyenYüzdesi = (kötüleyen/toplam)*100

NPS = desteyelenYüzdesi-kotuleyenYüzdesi

print("NPS değeriniz",NPS)


