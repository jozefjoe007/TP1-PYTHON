n=int(input("saisir un nombre entier : "))
p = int(input(f"entrer la puissance de {n} : "))
if (n < 0) or (p < 0):
    print("Nombre négatif Fin de la saisie !\n") 
else:
    print(f"le resultat de {n} à la puissance {p} est : {n**p}")