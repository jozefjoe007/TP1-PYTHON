# Programme calculant la somme d'une suite d'entiers terminée par 0

somme = 0

print("Entrez une suite d'entiers (tapez 0 pour terminer et obtenir la somme) :")

while True:
    nombre = int(input("Entrez un nombre : "))
    
    # Si le nombre entré est 0, on arrête la boucle
    if nombre == 0:
        break
    
    # On ajoute le nombre à la somme
    somme += nombre

# Affichage du résultat avec écriture formatée (f-string)
print(f"La somme de la suite d'entiers est : {somme}")
