from math import ceil, floor

def intéressant(n):
    chiffres = []
    j = n
    while j >= 1:
        chiffres.append(j % 10)
        j //= 10
    chiffres.reverse()
    
    partie1 = 0
    partie2 = 0
    for i in [0, 1]:
        partie1 += chiffres[i] * 10 ** (1-i)
    for i in [2, 3]:
        partie2 += chiffres[i] * 10 ** (3-i)
    
    if 2 * partie1 == partie2:
        return True
    return False


def divise(n, liste):
    for i in liste:
        if floor(i/n) != ceil(i/n):
            return False
    return True


nombreIntéressant = [i for i in range(1000, 10000) if intéressant(i)]
diviseurs = [i for i in range(1, 5000) if divise(i, nombreIntéressant)]
print(diviseurs[-1])