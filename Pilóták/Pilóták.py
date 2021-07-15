
import io
from Adatok import *

lista = []
with open("pilotak.csv",  encoding="utf-8")  as beolvas:
    fejlec = beolvas.readline()
    sorok = beolvas.read().splitlines()
beolvas.close()
for x in sorok:
        lista.append(Adatok(x))
print("3. feladat: {}" .format(len(lista)))
print("4. feladat: {}" .format(lista[len(lista)-1].Nev))
print("5. feladat: ")
datum = dt.datetime(1901,1,1)
for x in lista:
    if x.Szuletes<datum:
        print("\t{} ({})".format(x.Nev, x.Szuletes.strftime("%Y. %m. %d.")))
min = 10000
for x in lista:
    if x.Rajtszam<min and x.Rajtszam!=0: min = x.Rajtszam
for x in lista:
    if x.Rajtszam==min : 
        print("6. feladat: {}".format(x.Nemzetiseg))
        break
valogatas = []
for x in lista:
    szamlalas =0
    for y in valogatas:
        if(y==x.Rajtszam):szamlalas+=1
    if szamlalas ==0 : valogatas.append(x.Rajtszam)
kivalogatott = []
for x in valogatas:
    megszamlalas =0
    for y in lista:
        if(x ==y.Rajtszam): megszamlalas+=1
    if(megszamlalas>1 and x!=0): kivalogatott.append(x)
print("7. feladat:", end=" ")
print(*kivalogatott, sep=", ")
input()
       
     


    

