import os

os.system("cls")
"""#Írjuk ki a számokat 10-200 ig tizesével egymás mellé
for i in range(10, 201, 10):
    print(i, end=" ")
print("")
for i in range(1, 21, 1):
    print(i*10, end=" ")
print("")
#Írjuk ki a Budapest szót, ahányszor a program felhasználója kéri
kiirdb=int(input("Hányszor írjam ki a Budapest szót?: "))
print("")
for i in range(1, kiirdb+1, 1):
    print(i,". Budapest", sep="")
print("")"""
#Írassa ki 100-50-ig visszafele az összes 5-tel osztható szám
#kétszeresét!
for i in range(100, 49, -1):
    if(i%5==0):
        print(i*2, end=" ")
print("")
for i in range(100, 49, -5):
    print(i*2, end=" ")
print("")
for i in range(200, 99, -10):
    print(i*2, end=" ")
print("")