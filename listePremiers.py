[print(i) for i in range(2, int(input("Valeur de n : "))+1) if len([j for j in range(1, i//2 + 1) if i % j == 0]) == 1]