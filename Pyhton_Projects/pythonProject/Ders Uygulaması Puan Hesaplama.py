def puanHesapla(dogru,yanlis,bos):
    toplamSoru = dogru+yanlis+bos
    if toplamSoru>100:
        print("Toplam Soru Sayınız 100'ü geçemez")
    else:
        puan = (4*dogru)+(-1*yanlis)
        print(f"Doğru:{dogru} Yanlış:{yanlis} Boş:{bos} Puan{puan}")

while True:
    d = int(input("Doğru sayınızı giriniz"))
    y= int(input("Yanlış sayınızı giriniz"))
    b= int(input("Boş sayınızı giriniz"))
    puanHesapla(d,y,b)