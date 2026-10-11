# Initialisation de la somme
somme = 0
compteur = 0

print("Entrez des nombres entiers négatifs (un nombre positif ou zéro arrêtera la saisie) :")

while True:
    nombre = int(input("Entrez un nombre entier : "))
    
    if nombre >= 0:
        print("Nombre positif ou zéro détecté. Fin de la saisie !\n")
        break 
    
    somme += nombre
    compteur += 1

# Affichage du résultat avec écriture formatée (f-string)
print(f"Vous avez saisi {compteur} nombre(s) négatif(s).")
print(f"La somme des entiers négatifs saisis est : {somme}")