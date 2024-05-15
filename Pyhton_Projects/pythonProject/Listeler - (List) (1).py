#Listeler - Array

not1 = 50
not2 = 60
not3 = 70

ort = (not1+not2+not3)/3

#############

ogrenci1 = [50,60,70,"burak",10.6]

#Listelerin içerisinde tek bir veri tipi
#olmak zorunda değil

#Verileri çağırmak için index-1
notlar = [30,20,45]
#          0  1  2

#Verileri çağırmak için index-2
notlar = [45,32,12]
#         -3 -2 -1

print(notlar[0])
print(notlar[-1])

#listenin eleman sayısı için
print(len(notlar))

#Listenin ilk elemanına ulaşmak için
print(notlar[0])
print(notlar[-len(notlar)])

#Listenin son elemanına ulaşmak için
print(notlar[-1])
print(notlar[len(notlar)-1])

liste = ["İbrahim","Elif",12,35]

#Listelerin değerleri değiştirilebilir

liste[1] = "Emirhan"

print(liste)

#Listenin en büyük değeri

liste = [1,2,3,54,76,7,9,95,150]

print(max(liste))

#Listenin en küçük değeri

print(min(liste))

#Listenin sıralaması

liste.sort() #Küçükten Büyüğe sıralama yapar
print(liste)

liste.sort(reverse=True)
print(liste)

#listenin en küçük değeri
liste[-1]
liste[len[liste]-1]

#listenin en büyük değeri
liste[0]
liste[-len(liste)]

#En büyük değer ile en küçük değer arasındaki fark

numbers= [1,45,4,65,32,12,56]

#1. Yöntem
numbers.sort()
fark = numbers[-1]-numbers[0]
print(fark)

#2. Yöntem
mak = max(numbers)
mi = min(numbers)
fark = mak-mi
print(fark)




