bad = int(input("Lütfen kötü yorum sayısını giriniz :"))
notr = int(input("Lütfen nötr yorum sayısını giriniz :"))
good = int(input("Lütfen iyi yorum sayısını giriniz :"))

fullperson = bad + good + notr

destek = (good/fullperson)*100
zarar = (bad/fullperson)*100
nps = destek-zarar
nps =int(nps)
print("..........NPS puanınız hesaplanıyor..........\n"
      "işte *NPS* puanını = ",nps)
