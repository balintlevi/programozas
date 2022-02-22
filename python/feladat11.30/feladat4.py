import os
import random

os.system("cls")
magassagok=[0]*16
print(magassagok)
for i in range(0, 16, 1):
    magassagok[i]=random.randrange(160,183)
    print(magassagok[i], end=" ")