import os

os.system("cls")
#Szöveg bekérés, számoljk meg, hpgy hányszóköz nélüli karakterünk, ill. hányszavunk van!
szoveg=input("Adjon meg egy szöveget: ")
szokozdb=0
for i in range(0, len(szoveg), 1):
    if(szoveg[i]==" "):
        szokozdb=szokozdb+1
karszam=len(szoveg)-szokozdb
szavakszama=szokozdb+1
print("A szövegben", karszam,"szóköz nélküli karakterünk van")
print("A szövegben", szavakszama, "szavunk van")