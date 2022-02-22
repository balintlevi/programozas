import os
import random

def afeladat(s1, s2):
    if(s1%2==0 and s2%2==0):
        if(s1>s2):
            sz=((s1-s2)/s2)*100
            print("Eltérés: ", sz, "%")
        else:
            sz=((s2-s1)/s1)*100
            print("Eltérés: ", sz, "%")
    else:
        h=s1/s2
        print(round(h, 3))

def bfeladat(s1,s2):
    maradek=s1%s2
    eredmeny=maradek%2
    if(eredmeny==0):
        return "Páros"
    else:
        return "Páratlan"

def dfeladat(solista):
    elteresek=[]
    for i in range(0, len(solista), 1):
        elteresek.append(abs(solista[i]-35))
    return elteresek

def efeladat(solista):
    solista=list(set(solista))
    solista.sort()
    for i in range(0, len(solista), 1):
        print(solista[i], end=" ")

os.system("cls")
so1=int(input("1. sótartalom: "))
so2=int(input("2. sótartalom: "))
#A. FELADAT ELJÁRÁSSAL
print("a.) feladat")
afeladat(so1,so2)
#B. FELADAT FÜGVÉNNYEL
print("b.) feladat")
print(bfeladat(so1,so2))
#C FELADAT
print("c.) feladat")
sotartalmak=[]
for i in range(0, 20, 1):
    sotartalmak.append(random.randrange(30, 41))
print(*sotartalmak)
#D FELADAT
print("d.) feladat")
print(*dfeladat(sotartalmak))
#E FELADAT ELJÁRÁSSAL
print("e.) feladat")
efeladat(sotartalmak)