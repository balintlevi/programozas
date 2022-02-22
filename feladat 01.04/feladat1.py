import os
import random
os.system("cls")
lista=[]
#szoveg karakterszáma
betuszam=random.randrange
print(betuszam)
#karakterkódok előállítása
for i in range(0, betuszam,1):
    lista.append(random.randrange(97, 123))
    print(lista)
#karakterkódok
for i in range(0, len(lista), 1):
    lista[i]=chr(lista[i])
print(lista)
for i in range(1, 11, 1):
    csereindex=random.randrange(1, len(lista, -1))
    if(csereindex%2!=0):
        lista[csereindex]=" "
print(lista)
for i in range(1, len(lista, 2)):
    lista[i]=lista[i].upper()
    print(lista)
    #szöveg kiírása
s="". join(lista)
print(s)
#szöveg második szava
masodikszo=s.split()[1]
print(masodikszo)