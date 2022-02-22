import os
import random

def kiszamol(aoldal, boldal):
    return aoldal*boldal

os.system("cls")
aoldal=random.randrange(50, 101)
boldal=random.randrange(100, 151)
print(aoldal)
print(boldal)
print("A téglalap területe:", kiszamol(aoldal, boldal), "cm2")