import os

os.system("cls")
#számok kiiratása 1-20 ig
for i in range(1,21, 1):
    print(i, end=" ")
print("")
#számok kiiratása 1-20 ig (csak páratlanok)
for i in range(1, 20, 2):
    print(i, end=" ")
print("")
for i in range(1, 20, 1):
    if(i%2!=0):
        print(i, end=" ")
print("")
#számok kiiratása 1-20 ig (csak páros)
for i in range(2, 21, 2):
    print(i, end=" ")
print("")
for i in range(2, 21, 1):
    if(i%2==0):
        print(i, end=" ")
print("")
#számok 20-1 ig visszafele
for i in range(20, 0, -1):
    print(i, end=" ")
print("")
#számok 20-1 ig visszafele párosak
for i in range(20, 1, -2):
    print(i, end=" ")
print("")
#számok 20-1 ig visszafele páratlanok
for i in range(19, 0, -2):
    print(i, end=" ")
print("")
#számok 1-20 ig (i=10 nél ciklus megszakítás)
for i in range(1, 21, 1):
    print(i, end=" ")
    if(i==10):
        break
print("")
#számok 1-20 ig  (ha i 5-el osztható, akkor nem írjuk ki)
for i in range(1, 21, 1):
    if(i%5==0):
        continue
    print(i, end=" ")
print("")
