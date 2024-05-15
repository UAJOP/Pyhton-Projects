notlar = []

not1 = float(input("1. notunuzu giriniz"))
notlar.append(not1)
not2 = float(input("2. notunuzu giriniz"))
notlar.append(not2)
not3 = float(input("3. notunuzu giriniz"))
notlar.append(not3)

print(notlar)

ort = sum(notlar)/len(notlar)
print("Ortalama",ort)