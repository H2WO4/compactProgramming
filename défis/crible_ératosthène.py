liste = [*range(2, int(input("Entrez N : ")))]
liste = [set([j for j in liste if (j % i != 0) or (j == i)]) for i in liste[0:len(liste)//2]]
while len(liste) > 1:
    liste = [liste[i-1] & liste[i] for i in range(1, len(liste))]
print(liste[0])