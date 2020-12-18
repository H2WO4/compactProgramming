def reprAscii(mot):
    output = []
    for char in mot:
        output.append(ord(char))

    return output

def reprCode(liste):
    mot = ""
    for k in liste:
        mot += chr(k)
    
    return(mot)

print(a := reprAscii("ABCDEZçabcdez"))
print(reprCode(a))