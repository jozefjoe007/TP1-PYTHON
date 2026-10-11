n = int(input("Entrez un nombre entier : "))
f = n * n
pair = (f % 2 == 0)

print(f"Le carré du nombre {n} est {f}")

if f % 2 == 0:
    print(f"Est-ce que {f} est pair ? : {pair}")
else:
    print(f"Le carré de {f} est pair ? : {pair}")
