import os

os.system("cls")
#Írjunk ki 5*5 csillag csoportot!
for i in range(1, 6, 1):
    for j in range(1, 6, 1):
        print("*", end="")
    print("")
input("")
os.system("cls")
#15*15  -ös szorzótábla
for i in range(1, 16, 1):
    for j in range(1, 16, 1):
        print("{0:>3}" .format(i*j), end=" ")
    print("")