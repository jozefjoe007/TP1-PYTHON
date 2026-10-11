while True:
    # Saisie et validation du nombre
    while True:
        try:
            n = int(input("Entrez un nombre entier entre 0 et 10 : "))

            if n < 0 or n > 10:
                print("Erreur : Le nombre doit être compris entre 0 et 10.")
            else:
                break
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

    # Calcul de la factorielle
    factorielle = 1

    for i in range(1, n + 1):
        factorielle = factorielle * i

    # Affichage du résultat
    print(f"La factorielle de {n} ({n}!) est : {factorielle}")

    # Demander si l'utilisateur veut recommencer
    choix = input("Voulez-vous calculer une autre factorielle ? (o/n) : ")

    if choix.lower() != "o":
        break

print("Au revoir !")
