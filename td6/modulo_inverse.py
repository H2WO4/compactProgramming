from math import isqrt

def diviseurs(n):
    diviseurs = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            diviseurs.append(i)
            if n // i != i:
                diviseurs.append(n//i)

    return set(diviseurs)

def invModulo(n, m):
    for i in range(m):
        if (n * i) % m == 1:
            return i
    else:
        return n

print(invModulo(4, 13))