liste, poids = eval(input("Entrez une liste : ")), eval(input("Entrez la liste des poids : "))
print(sum([poids[j] * liste[j] for j in range(len(poids))])/sum(poids))