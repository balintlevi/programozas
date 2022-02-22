import os

os.system("cls")
print("STRING MŰVELETEK")
s1="Csokonai Vitéz Mihály"
print("A költő neve: ", s1)
#Írjuk ki a harmadik karaktert
print("A harmadik karakter: ", s1[2])
#Írjul ki a középső nevet (Vitéz)
print("A középső név: ", s1[9: 14])
print("A középső név: ", s1.split()[1])
#A középső név kezdete (pozíciója)
print("A középső név kezdete: ",s1.find("Vitéz")+1)
#A szöveg hossza
print("A költő nevének hossza: ", len(s1))
#Hozzáfűzés 
s1=s1+" költő"
print("Hozzáfűzés után: ", s1)
#"o" betű beszúrása első név után
s1=s1.split()[0]+"o"+s1[8:27]
print("o beszúrás után: ",s1)
#"o" betű törlése
s1=s1[0:8]+s1[9:28]
print("o törlése után: ",s1)
#csere
print("Csere után", s1.replace("V", "v"))