import os
import math

def felulet(sugar, magassag):
    return(2*sugar*sugar*math.pi)+(magassag*2*sugar*math.pi)

def festek():
    return(2*felulet(r,m))/100

def viz(sugar, magassag):
    return(sugar*sugar*math.pi*magassag)*0.9

def vizliter():
    return viz(r,m)/1000

os.system("cls")
r=float(int(input("Adja meg a vödör alapkörének sugarát: ")))
m=float(int(input("Adja meg a vödör magasságát: ")))
print("")
print("A vödör felülete: ", round(felulet(r, m), 3), "cm2")
print("Szükséges festék: ", round(festek(),3), "kg")
print("Víz mennyisége: ", round(viz(r,m), 3), "cm3")
print("A víz mennísége2: ", round(vizliter(), 3), "liter")
