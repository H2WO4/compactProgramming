import os

os.chdir(os.getcwd() + "/td6")

def decode(char, key = -1):
    if ord(char) in range(65, 91):
        return chr(((ord(char) + key - 65) % 26) + 65)
    elif ord(char) in range(97, 123):
        return chr(((ord(char) + key - 97) % 26) + 97)
    else:
        return char

with open("text.txt", "r", encoding="utf-8") as f:
    while (line := f.readline()) != "":
        print(line.strip("\n"))
    
    print()
    f.seek(0)
    output = ""
    for i in f.read():
        output += decode(i)

    with open("textDecoded.txt", "a", encoding="utf-8") as w:
        w.write(output)