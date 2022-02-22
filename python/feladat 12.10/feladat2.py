import os

os.system("cls")
szavak=[]
for i in range(0, 7, 1):
    szavak.append(input(str(i+1)+". szó: "))
print("")
keresettszo=input("Keresett szó: ")
for i in range(1, 7, 1):
    if(keresettszo==szavak[i]):
        print("Keresett sorszáma: ",i)