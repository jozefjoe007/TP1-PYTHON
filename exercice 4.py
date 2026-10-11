texte = input("Entrez un mot ou une phrase : ")
texte_majuscule = texte.upper()
voyelles = "AEIOUYaieouy"
nb_voyelles = 0
for caractere in texte_majuscule:
    if caractere in voyelles:
        nb_voyelles += 1
print(f"Texte en majuscules : {texte_majuscule}")
print(f"Nombre de voyelles contenues : {nb_voyelles}")
