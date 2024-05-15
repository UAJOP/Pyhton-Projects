# calismasure = [15,10,24,34,
#                25,15,10,5,
#                35,45,0,12,
#                30,15,65,75,
#                12,15,17,12,
#                100,120,125,90]
#
# GP=calismasure[0:24:4]
# VTYS=calismasure[1:24:4]
# NTP=calismasure[2:24:4]
# MP=calismasure[3:24:4]
#
#
# VTYS[1]=20
# NTP[2]=5
# VTYS[3]=20
# """
# print(VTYS)
#
# for i in GP:
#     print(i,end=' ')
# """
# print(max(VTYS))
#
# print(sum(VTYS)/len(VTYS))
def hesap2():
    apg2 = int(input("APG 2 Değerini gir"))
    pg = int(input("PG Değerinizi Girin"))
    if apg2 < 100 and 140 < pg < 199:
        print("İzole BGT")
    elif 100 < apg2 < 125 and pg < 140:
        print("İzole BAG")
    elif 100 < apg2 < 125 and 140 < pg < 199:
        print("BAG ve BGT")
    elif apg2 >= 126 and pg > 200:
        print("Diyabetsin")
def hesap1():
    while True:
        apg1=int(input("APG1 değerini gir :"))

        if apg1<100:
            print("Sonucunuz Normal")
        elif 100<apg1<126:
            print("Sizi OGTT testine yönlendiriyorum")
            hesap2()
        else:
            print("Diyabet Hastasısınız")
        break






hesap1()
















