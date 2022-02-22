#Bekérünk 2 számot
#Írjuk ki melyik a nagyobb(egyenlőséget vizsgálunk)
#adabeker - eljaras, nagyobb - eljaras

import os

def adatbeker():
    global szam1, szam2
    szam1=int(input("Szám1: "))
    szam2=int(input("Szám1: "))
    print("")

def nagyobb():
    if(szam1>szam2):
        print("A nagyobb szám: ", szam1)
    elif(szam1<szam2):
        print("A nagyobb szám: ", szam2)
    else:
        print("A két szám egyenlő!")

os.system("cls")
adatbeker()
nagyobb()