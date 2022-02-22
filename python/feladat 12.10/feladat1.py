import os
import random

os.system("cls")
jegyszamok=[0]*14
print("Elado jegyek szama: ")
for i in range(0, len(jegyszamok), 1):
    jegyszamok[i]=random.randrange(10, 237)
    print(jegyszamok[i], end=" ")
print("\na.) feladat")
vane=False
for i in range( 0, 7, 1):
    if(jegyszamok[i]%2!=0 and jegyszamok[i]%3==0):
        print(jegyszamok[i], end=" ")
        vane=True
if(vane==False):
    print("Nincs ilyen szám!", end=" ")
else:
    print("Van ilyen")
print("\nb.) feladat")
for i in range(7, 14, 1):
    if(jegyszamok[i]>60 and jegyszamok[i]<186):
        print(jegyszamok[i], end=" ")
print("\nc.) feladat")
if(jegyszamok[1]>jegyszamok[12]):
    print("A 2. eladás a nagyobb")
else:
    print("A 13. eladás a nagyobb")
    kisebb=jegyszamok[1]
print("Összeg: ", kisebb+jegyszamok[2])
print("d.) feladat")
print("Legtöbb jegyzsám:", max(jegyszamok))
print("f.) feladat")
print("Átlag: ", round(sum(jegyszamok)/len(jegyszamok),3))