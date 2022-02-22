import os

def vonal(hossz, jel):
    print("")
    for i in range(1,hossz,1):
        print(jel, end=" ")
    print("\n")

os.system("cls")

print("a.) feladat")
vonal(50, "*")
print("b.) feladat")
vonal(70, "$")
print("c.) feladat")
vonal(40, "/")