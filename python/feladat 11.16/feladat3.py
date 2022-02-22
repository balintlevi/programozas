import os

os.system("cls")
#Szöveg + karakterbekérés, a program írja ki a karakter szövegben való előfordulásait.
#Ha egyszer se fordul elő, akkor kiírjuk, hogy "nincs találat"
szoveg=input("Adjon meg egy szöveget: ")
keresett=input("Keresett karakter: ")
print("")
vane=False
print("A keresett karakter poziciói: ")
for i in range(0, len(szoveg), 1):
    if(szoveg[i]==keresett):
        print("Pozició: ", i+1)
        vane=True
if(vane==False):
    print("Nincs találat")