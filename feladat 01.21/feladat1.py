import os
import random

def adatgeneralas():
    global aoldal, boldal
    aoldal=random.randrange(50, 101)
    boldal=random.randrange(100,151)
    print("a oldal: ", aoldal, "cm")
    print("b oldal: ", boldal, "cm")
    print("")

def kiszamol():
    return aoldal*boldal

os.system("cls")
adatgeneralas()
print("A téglalap területe:", kiszamol(), "cm2")