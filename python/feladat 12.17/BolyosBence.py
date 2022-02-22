import os
import random

os.system("cls")
#12 napon át hányan utaztak, véletlenszámgenerálás 20-45
nap=[0]*12
print("A vonattal utazók száma Budapesttől Debrecenbe: ")
print("a) feladat: ")
for i in range(1, len(nap), 1):
    nap[i]=random.randrange(20,45)
    print(nap[i], end=" ")
#A harmadik vagy az ötödik napon utaztak -e többen?
print("\nb) feladat: ")
if(nap[3] > nap[5]):
    nagyobb=nap[5]
    print("Az ötödik vonaton utaztak többen: ")
else:
    kisebb=nap[3]
    print("A harmadik napon utaztak többen: ")


"""for i in range(0, 2, 1):
    if(nap[i] % 3 !=0 and nap[i] % 5 ==0):
        print(nap[i], end=" ")
        vane=True
if(nap[3] > nap[5]):
    print("Az harmadik napon utaztak többen: ")
elif(nap[3] < nap[5]):
    print("Az ötödik napon utaztak többen: ")
else:
    print("Mind a két alkalommal ugyanannyian utaztak a vonaton")
#31 feletti páratlan utaszámok
print("\nc) feladat: ")
for i in range(30, len(nap), 1):
    print(i)
print("\nd) feladat: ")
print("\ne) feladat: ")
print("\nf) feladat: ")"""