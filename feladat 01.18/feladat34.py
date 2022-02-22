import os

def adatbevitel():
    global aoldal, boldal
    aoldal=int(input("Kérem az a oldalt: "))
    boldal=int(input("Lérem a b oldalt: "))
    print("")

def kiszamol():
    terulet=aoldal*boldal
    print("A téglalap területe: ", terulet)

os.system("cls")
adatbevitel()
kiszamol()