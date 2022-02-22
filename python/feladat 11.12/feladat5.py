import os
import random

os.system
#Generáljunk egy számot 1-10 között. A program felhasználójának ki kell találnia, hogy melyik számra
#gondolt a gép. Azt is írjuk ki, hogy hányadikk lépésben találta ki
szam=random.randrange(1, 11)
lepes=1
print("Gondoltam egy számot 1-10 között, találd ki melyik az!")
tipp=int(input("Tipp: "))
while(tipp!=szam):
    if(tipp>szam):
        print("Nem jó a tipp, mert túl nagy")
    else:
        print("Nem jó a tipp, mert túl kicsi")
    lepes=lepes+1
    tipp=int(input("Tipp: "))
print("Kitalálta a gondolt számot: ", szam)
print("Gratulálunk," ,lepes,"lépésben sikerült!")