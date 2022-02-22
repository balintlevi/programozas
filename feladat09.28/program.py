import os
import random
import math

os.system("cls")
"""magassag1=185 #értékadás
magassag2=200
atlag=(magassag1+magassag2)/2
#print("a 2 ember átlagmagassága:",atlag)
#print("a 2 ember átlagmagassága: "+str(atlag))
#print("a 2 ember átlagmagassága: {atlag}")
print("a 2 ember átlagmagassága: {0}".format(atlag))
input("") #beolvadás (felhasználó ad értéket)
os.system("cls")
magassag1=int(input("Adja meg az első személy magasságát: "))
magassag2=int(input("Adja meg az első személy magasságát: "))
atlag=(magassag1+magassag2)/2
print(f"a 2 ember átlagmagassága: {atlag}")
input("") #véletlen szám érték (160 - 200)"""
os.system("cls")
#magassag1=random.randrange(160, 201)
#magassag2=random.randrange(160, 201)
magassag1=random.random()*40+160 #első szám: végérték-kezdőérték
magassag2=random.random()*40+160 #második szám: kezdőérték
print("A 2 véletlen magasság:", magassag1,"és",magassag2)
atlag=round((magassag1+magassag2)/2,2) #mindig lefele egészre kerekít
#print(f"a 2 ember átlagmagassága: {atlag}")
atlag=math.ceil(atlag) #mindig felfele egészre kerekít
print(f"a 2 ember átlagmagassága: {atlag}")
atlaggyok=math.sqrt(atlag)
print("Az átlag gyöke:",atlaggyok)