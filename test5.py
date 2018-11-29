import math

a=float(input("Unesite vas prvi broj: "))
b=float(input("Unesite vas drugi broj: "))
op=input("Odaberite operaciju: ")

if op== "zbrajanje":
    print("Rezultat vaseg racuna je " + str(a+b) + ".")
elif op== "oduzimanje":
    print("Rezultat vaseg racuna je " + str(a-b) + ".")
elif op== "množenje":
    print("Rezultat vaseg racuna je " + str(a*b) + ".")
elif op== "dijeljenje":
    print("Rezultat vaseg racuna je " + str(a/b) + ".")
elif op== "korijen":
    print("Korijen broja " + str(a) + " je " + str(math.sqrt(a)) + ".")
elif op== "kvadrat":
    print("Kvadrat broja " + str(a) + " je " + str(pow(a,2)) + ".")
elif op== "usporedivanje":
    if str(a)>str(b):
        print("Veci broj je " + str(a) + ".")
    else:
        print("Veci broj je " + str(b) + ".")
else:
    print("Kalkulator ovo ne moze izracunati.")
