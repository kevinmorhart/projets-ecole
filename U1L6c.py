nombre_biscuits = int(input("Combien de biscuits veux-tu préparer?\t"))
coefficient = nombre_biscuits / 48

print(f"""Pour {nombre_biscuits} biscuits, il te faudra:
\t{round(coefficient*1.5, 2)} tasses de sucre
\t{round(coefficient*1, 2)} tasses de beurre
\t{round(coefficient*2.75, 2)} tasses de farine""")