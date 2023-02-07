import math

try:
    personnes = int(input("\nNombre d'invités:\t"))

    paquet_c = 10
    paquet_p = 8

    min_c = personnes / paquet_c
    min_p = personnes / paquet_p

    reste_c = (math.ceil(min_c) - min_c) * paquet_c
    reste_p = (math.ceil(min_p) - min_p) * paquet_p

    print(f"\n{math.ceil(min_c)} paquets de chien-chauds seront requis, {int(reste_c)} resteront")
    print(f"{math.ceil(min_p)} paquets de petits pains à chien-chauds, {int(reste_p)} resteront")
except ValueError:
    print("Insérer un valeur de type \"string\"")
