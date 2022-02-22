import os

os.system("cls")
#6 elemű lista  -> számok bekéréssel
szamok=[0]*6
print(szamok)
for i in range(0,6,1):
    szamok[i]=int(input("Adjon egy számot: "))
print(szamok)
#Írjunk ki páros sorszámú elemeket!
for i in range(1, len(szamok), 2):
    print(szamok[i], end=" ")
#Írjuk ki 2-3 közül a párosokat
for i in range(3, 6, 1):
    if(szamok[i]%2==0):
        print(szamok[i], end=" ")