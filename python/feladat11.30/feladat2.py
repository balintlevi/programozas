import os

os.system("cls")
szamok=[3, 12, 11, 19, 5, 8, 17, 2, 1, 4]
print(szamok)
#A "2" érték hányadik a listában
print(szamok.index(2)+1)
#Töröljuk a harmadik elemet
del szamok [2]
print(szamok)
#Töröljük a 12-es szám értékét
szamok.remove(12)
print(szamok)
#Növelvő sorrend!
szamok.sort()
print(szamok)
#csökkenő sorrend
szamok.reverse()
print(szamok)