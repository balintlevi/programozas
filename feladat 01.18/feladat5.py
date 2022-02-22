import os

def beker():
    global szam1, szam2
    szam1=int(input("Kérem az első számot: "))
    szam2=int(input("Kérem a második számot: "))
    print("")

def muvelet():
    szam3=1
    szamitas=(szam1+szam2)-szam3
    print(szamitas)

os.system("cls")
beker()
muvelet()