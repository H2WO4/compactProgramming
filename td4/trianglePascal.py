triangle = [[1]]
[triangle.append([1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(i-1)] + [1]) for i in range(1, int(input("Nombre de colonnes du triangle : "))+1)]
[print(" ".join([str(j) for j in i])) for i in triangle]