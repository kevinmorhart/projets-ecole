kilometres = float(input("Inscris le nombre de kilomètres parcourus: "))
gallons = float(input("Inscris le nombre de gallons utilisés: "))

milles = kilometres / 1.609344
litres = gallons * 4.54609 # us gallon 3.78541

print(f"""L'efficacité est de: 
\t{round(milles/gallons, 1)} mi/gal
\t{round(kilometres/litres, 1)} km/L

Pour comparer au statistiques EnerGuide:
\t{round(litres/(kilometres/100), 1)} L/100 km
""")