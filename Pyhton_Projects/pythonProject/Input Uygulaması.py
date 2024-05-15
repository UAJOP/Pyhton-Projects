anapara = float(input("Anaparanızı giriniz"))
faizOrani = float(input("Faiz oranını giriniz"))
gün = int(input("Kaç günlük faiz hesaplamak istersiniz"))

faizMiktari = (anapara/100)*(faizOrani/365)*gün
#faizMiktari = int(faizMiktari)
print(f"""
Anaparanız {anapara},
Faiz Oranı %{faizOrani},
Gün Sayısı {gün},
Kazancınız {int(faizMiktari)}
""")

