def minimumListe(liste):
    minimum, index = [liste[0]], [0]
    [[minimum.append(liste[i]), index.append(i)] for i in range(1, len(liste)) if liste[i] <= minimum[-1]]
    return (minimum[-1], index[-1])
occurencesMinimum = lambda liste: [i for i in range(len(liste)) if liste[i] == minimumListe(liste)[0]]
print(minimumListe(eval(input("Entrez une liste : "))))
print(occurencesMinimum(eval(input("Entrez une liste : "))))