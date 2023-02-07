# La méthode 'input' stocke par défaut une valeur de type string:
ma_variable = input("Écris un nombre: ")
print("Type de la saisie: ", type(ma_variable))

# Il faut alors convertir Ie type str int:
a = int(input("\nQuel est le premier nombre? "))
b = int(input("Que1 est le deuxiéme nombre? "))

# Division euclidienne:
quotient = a // b
reste = a % b

# Division exacte:
division = a / b

# Affichage des résultats:
print("\nLe quotient de la division euclidienne est:", quotient)
print("Le reste de la division euclidienne est:", reste)
print("Le résultat de la division exacte est:", division)

print("Type du quotient euclidien est: ", type(quotient))
print("Type du reste euclidien: ", type(reste))
print("Type du quotient: ", type(division))
