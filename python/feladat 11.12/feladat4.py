import os
os.system("cls")
ujra="i"
while(ujra=="i"):
    szam1=int(input("Szám1: "))
    szam2=int(input("Szám2: "))
    osszeg=szam1+szam2
    print("számok összege: ", osszeg, "\n")
    ujra=input("Akarsz -e még egyetszámolni?(i/n)")
    os.system("cls")