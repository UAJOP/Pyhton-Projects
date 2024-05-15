pzt = int(input("PAZARTESİ kaç soru çözdün ? :"))
sl = int(input("SALI kaç soru çözdün ? :"))
çrb = int(input("ÇARŞAMBA kaç soru çözdün ? ="))

sorular = []

sorular.append(pzt)
sorular.append(sl)
sorular.append(çrb)

print("GÜNCEL LİSTE :", sorular)

ort = sum(sorular)/len(sorular)
ort =int(ort)
print("Ortalama soru sayın :", ort)
