havadurumu = [25,30,17,27,
              24,35,12,18,
              14,15,19,21,
              31,35,38,42,
              24,27,26,29,
              34,38,39,41,
              9,10,4,7]

izmir =havadurumu[0:28:4]
istanbul=havadurumu[1:28:4]
ankara=havadurumu[2:28:4]
bursa=havadurumu[3:28:4]

izmir[6]+=5
print(izmir)
izmir[5]=39
print(izmir)
print("İzmir Hava durumu")
print("-******-")
for i in izmir:
    print(i)

print(sum(izmir)/len(izmir))

