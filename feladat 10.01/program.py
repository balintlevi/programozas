import os
import math

os.system("cls")
percido=int(input("kérem az időt percben: " ))
fonalhossz=int(input("Kérem a fonál hosszát:" ))
lengido=2*math.pi*math.sqrt(fonalhossz/9.81)
secido=percido*60
teljeslengszam=secido/lengido
print("A teljes lengeések száma adott idő alatt",round(teljeslengszam,2))