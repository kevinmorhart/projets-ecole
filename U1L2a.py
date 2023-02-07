# Saisies de l'utilisateur
# Rappel: La méthode input() retourne un string.
# II faut convertir les strings en int ou float.
x = float(input("Premier nombre:\t"))
y = float(input("\nDeuxième nombre:\t"))

#Calculs
somme = x + y
diff = x - y
prod = x * y
quot = x / y

# Résultats
print("\nRésultats:")
print("-------------------")
print(f"Somme: {x} + {y} = {somme}")
print(f"Difference: {x} - {y} = {diff}")
print(f"Produit: {x} * {y} = {prod}")
print(f"Quotient: {x} / {y} = {quot}")
