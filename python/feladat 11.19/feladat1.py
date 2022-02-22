import os

os.system("cls")
#a
s1="Kenyeret ettem meggyel"
e=0
for i in range(0, len(s1),1):
    if(s1[i]=="e"):
        e=e+1
print("az e betű mennyisége a szövegben: ", e)
#b
s2="kenyeret ettem meggyel"
print("Ma", s1[0:0])