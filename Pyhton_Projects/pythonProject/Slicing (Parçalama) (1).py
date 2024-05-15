#Slicing - Parçalama

notlar = [60,50,10,70,60,20,90,80,90]
#         0  1   2  3  4  5  6 7  8

GP = notlar[0:3]
NTP = notlar[3:6]
YZ = notlar[6:9]

print("GP", GP)
print("NTP",NTP)
print("YZ", YZ)

print("Vizeler",GP[0],NTP[0],YZ[0])

#GP dersinin finali 10 eksik yazıldığı için günceleme yapıyoruz
GP[2]= 20

"""
GP
Vize %40
Projenin %20
Finalin %40
"""
ort = (GP[0]*40/100)+(GP[1]*20/100)+(GP[2]*40/100)

print("""
GP için
Vize: {0}
Proje: {1}
Final: {2}
Geçme Notu: {3}

""".format(GP[0],GP[1],GP[2],ort))

