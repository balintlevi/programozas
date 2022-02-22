import os
import random

def afeladat(e1,e2,e3):
    """#1.megoldás
    if(e1>e2 and e1>e3):
        return e1
    elif(e2>e1 and e2>e3):
        return e2
    else:
        return e3"""
    #2 megoldás
    legnagyobb=max(e1,e2,e3)
    return legnagyobb

def bfeladat(e1,e2):
    fogyasztft=int(input("1 kg eledel ára FT-ban: "))
    earfolyam=random.randrange(340, 371)
    print("1 euro", earfolyam, "FT")
    kifizet=(((e1+e2)*fogyasztft)/earfolyam)
    print("Az ellatas ára euróban", kifizet, "euro")
    if(kifizet%2==0):
        print("A kifizetendő euro értéke páros")
    else:
        print("A kifitetendő euro értéke páratlan")

def  dfeladat(allatok):
    """for i in range(0, len(allatok), 1):
        if(allatok[i]==218):
            print("218 kg eledel a(z)", i+1, ". elefánt evett", sep="")"""
#2 megoldas
enyitevett=allatok.index(218)+1
print("218 kg eledel a(z)", enyitevett, ". elefánt evett")

os.system("cls")
elefant1=random.randrange(202, 241)
elefant2=random.randrange(202, 241)
elefant3=random.randrange(202, 241)
print("Elefántok napi fogyasztása (kg): ")
print(elefant1, elefant2, elefant3)
#A.) Feladat FÜGGVÉNNYEL
print("a.) feladat")
print(afeladat(elefant1, elefant2, elefant3))
#B.) FELADAT
print("b.) feladat")
bfeladat(elefant1, elefant2)
#C FELADAT
print("c.) feladat")
elefantok=[222, 231, 211, 238, 233, 218, 212, 214, 220, 223]
print(*elefantok)
#D FELADAT
print("d.) feladat")
