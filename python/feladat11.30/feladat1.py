import os

os.system("cls")
autok=["Ford", "Renault", "Opel"]
#Elemek kiiratása
print(autok)
print(*autok)
for i in range(0, len(autok), 1):
    print(autok[i], end=" ")
print("")
#Írassuk ki a 3. elemet!
print(autok[2])
#bővítsuk a listát -> Audi
autok.append("Audi")
print(autok)
#Audi -> Dacia
autok[3]="Dacia"
print(autok)
