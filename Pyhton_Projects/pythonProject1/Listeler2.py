
notlar = [50,70,90]
notlar.append(100)
#Listeye veri ekleme append
print(notlar)
not1 = int(input("Notunuzu giriniz :"))
print("GÜNCEL LİSTE :", notlar)
notlar.append(not1)
print(" Güncel liste :", notlar)

#Listeden veri silme pop
print("GÜNCEL LİSTE :", notlar)
notlar.pop() #listenin son elamanını siler
print("Güncel liste :" ,notlar)

notlar = [50,70,90,78,94]
print("GÜNCEL LİSTE :", notlar)
notlar.pop(3) #ilgili indexi siler
print("GÜNCEL LİSTE :", notlar)

#değer bazlı listedeki index numarası değilde listedeki elamının değerini siliyor

notlar = [50,70,3,12,56,88]
print("GÜNCEL LİSTE :", notlar)
notlar.remove(12)
print("GÜNCEL LİSTE :", notlar)


