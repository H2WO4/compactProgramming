def check(n):
    chiffres = []
    inverse = 0
    j = n
    while j >= 1:
        chiffres.append(j % 10)
        j //= 10
    
    l = 0
    for k in chiffres:
        inverse += k * 10 ** (len(chiffres) - l - 1)
        l += 1
    somme = n + inverse

    while somme >= 1:
        if somme % 2 == 0:
            return False
        somme //= 10
    return True

print([i for i in range(100, 1000) if check(i)][0])