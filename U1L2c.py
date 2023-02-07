nombre = int(input("Écris un entier:\t"))

if nombre > 0:
    print("Positif")
elif nombre < 0:
    print("Négatif")
else:
    print("Zéro")

if nombre % 2 == 0:
    print("Pair")
else:
    print("Impair")
