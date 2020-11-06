insertion = lambda liste, rang, élément: liste[:rang] + [élément] + liste[rang:]
mirroir = lambda liste: [liste[-i] for i in range(1, len(liste) + 1)]
coupe = lambda liste, rang1, rang2: [liste[i] for i in range(rang1, rang2 + 1 if rang1 < rang2 else rang2 - 1, 1 if rang1 < rang2 else -1)]
comptage = lambda liste, élément: len([i for i in liste if i == élément])
supression = lambda liste, rang: liste[:rang] + liste[rang + 1:]
print(insertion(eval(input("Entrez une liste : ")), int(input("Entrez le rang : ")), eval(input("Entrez un élément : "))))
print(mirroir(eval(input("Entrez une liste : "))))
print(coupe(eval(input("Entrez une liste : ")), int(input("Entrez le rang 1 : ")), int(input("Entrez le rang 2 : "))))
print(comptage(eval(input("Entrez une liste : ")), eval(input("Entrez un élément : "))))
print(supression(eval(input("Entrez une liste : ")), int(input("Entrez le rang : "))))