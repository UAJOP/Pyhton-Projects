notlar = [[82, 88, 80, 49, 62, 82],
          [68, 41, 93, 61, 54, 84],
          [74, 98, 65, 51, 74, 89],
          [64, 55, 89, 62, 72, 45],
          [50, 96, 45, 44, 94, 64]]


m_c_n = notlar[2][5]
print("Murat'ın coğrafya dersinden aldığı not:", m_c_n)


toplam_tarih_notlari = notlar[0][3] + notlar[1][3] + notlar[2][3]
print("Emel, Seda ve Murat'ın tarih dersinden aldıkları notların toplamı:", toplam_tarih_notlari)

fizik_notlari = [satir[1] for satir in notlar]
fizik_ortalama = sum(fizik_notlari) / len(fizik_notlari)
print("Fizik dersinin ortalaması:", fizik_ortalama)


y_not = 74
notlar[4][5] = y_not
print("Yeliz'in düzeltilmiş coğrafya notu:", y_not)
