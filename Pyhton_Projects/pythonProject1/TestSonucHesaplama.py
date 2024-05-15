def hesap( dogru , yanlis , bos):
    toplamSoruSayisi = dogru + yanlis + bos
    if toplamSoruSayisi > 25:
        print("Toplam soru sayınız 25'i geçemez....")
    else:
        puan = (4 * dogru) + (-1 * yanlis)
        print(f"Toplam Puanınız: {puan}   Toplam Soru Sayınız: {toplamSoruSayisi}")

while True:
    dogruU = int(input("Lütfen Doğru soru sayısınızı giriniz: "))
    yanlisU = int(input("Lütfen Yanlış soru sayınızı giriniz: "))
    bosU = int(input("Lütfen boş bıraktığınız soru sayısını giriniz: "))
    hesap(dogruU, yanlisU, bosU)


