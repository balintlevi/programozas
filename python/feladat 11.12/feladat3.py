import os

os.system("cls")
#Kérjünk be egy 10 és 20 közötti számot. Addig ismételjük a bekérést, 
#amíg jó számot ad meg a felhasználó
szam=int(input("Adjon meg egy 7-nél nagyobb számot: "))
while(szam>=10 or szam<=20):
    szam=int(input("Nem jó a megadott szám, kérem újra: "))