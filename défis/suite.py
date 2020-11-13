suite, continuation = ["1"], 0
for j in range(int(input("Quelle étape de la liste voulez vous voir : ")) - 1):
    suite.append("")
    for i in range(len(suite[j])):
        if continuation > 0:
            continuation -= 1
            continue
        try:
            if suite[j][i] == suite[j][i+1] == suite[j][i+2]:
                continuation = 2
                suite[-1] += "3{}".format(suite[j][i])
                continue
        except IndexError:
            pass
        try:
            if suite[j][i] == suite[j][i+1]:
                continuation = 1
                suite[-1] += "2{}".format(suite[j][i])
                continue
        except IndexError:
            pass
        suite[-1] += "1{}".format(suite[j][i])
print(suite[-1])