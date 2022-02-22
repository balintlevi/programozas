import os
import time

os.system("cls")
#Írjunk ki tíz darab csillag jelet a 10. oszlopba
for i in range(1, 11, 1):
    print("{0:>10}" .format("*"))
print("")
#Írjunk ki 10 db * jelet átlósan
for i in range(0, 10, 1):
    print(" "*i, "*", sep="")
print("")
#Írjunk ki 10 db * jelet átlósan visszafelé
for i in range(9, -1, -1):
    print(" "*i, "*", sep="")
print("")
#Írasson ki * jelekből egy 5 egység széles, 5 egység 
#magas "z" betűt!
for i in range(1, 6, 1):
    print("*", end="", flush=True)
    time.sleep(1)
print("")
for i in range(3, 0, -1):
    print(" "*i, "*", sep="")
    time.sleep(1)
for i in range(1, 6, 1):
    print("*", end="", flush=True)
    time.sleep(1)
print("")