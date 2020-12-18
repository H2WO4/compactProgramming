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

def codage(text, a, b):
    output = ""
    for char in text:
        output += chr((ord(char) * a + b) % 255)
    
    return output

def decodage(text, a, b):
    output = ""
    for char in text:
        output += chr(((ord(char) - b) * invModulo(a, 255)) % 255)
    
    return output

print(a := codage("abc", 3, 4))
print(decodage(a, 3, 4))

print(decodage(" ÂÚ’ ÂÚμ…ŽÎŠ ÞÂμ…ÞÂÚÒ…Š Þš î…Î¬ÚÒÒª…¶¡š æš Î’ ª’ š …– Ú…’ Â– Š ¢ª¾", 4, 5))