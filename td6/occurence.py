import os

os.chdir(os.getcwd() + "/td6")

with open("text.txt", "r") as f:
    occurences = 0
    character = "a"
    for char in f.read():
        if char.lower() == character.lower():
            occurences += 1
    
    print("The letter \"{}\" is found {} times in the document.".format(character, occurences))