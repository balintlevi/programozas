import os
import random

os.system("cls")
#Budapest kiíratása ötször
for i in range(1, 6, 1):
    print("Budapest", end=" ")
print("")
for i in range(10, 5, -1):
    print("Budapest", end=" ")
print("")
for i in range(10, 15, 1):
    print("Budapest", end=" ")
print("")
for i in range(10, 20, 2):
    print("Budapest", end=" ")
print("")
for i in range(1, 101, 1):
    print("Budapest")
print("")

#5 kockadobás eredménye
print("A dobások eredményei: ", end=" ")
for i in range(1, 6, 1):
    dobas=random.randrange(1, 7)
    print(dobas, end=" ")