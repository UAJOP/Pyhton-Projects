print(30+45)
print(30.4+45.6)
print(30+45.6)
#print("Burak"+35)  #Çalışmaz

kareninKenarı = 5
kareninAlanı = kareninKenarı*kareninKenarı
kareninÇevresi = kareninKenarı*4


dikdörtgeniKKenari= 5
dikdörtgeniBKenari=10

dikdörtgeninAlanı = dikdörtgeniKKenari*dikdörtgeniBKenari
dikdörtgeninCevresi = 2*(dikdörtgeniKKenari+dikdörtgeniBKenari)

print(""" Kenar uzunluğu {0} olan karenin çevresi {1} alanı {2} dır. 
Kısa kenarı {3} ve uzun kenarı {4} olan dikdörtgenin
Alanı: {5} Çevresi {6}'dır. 
""".format(kareninKenarı,kareninÇevresi,kareninAlanı,dikdörtgeniKKenari,dikdörtgeniBKenari,dikdörtgeninAlanı,dikdörtgeninCevresi) )