# FOR loop

name = input("Enter ur name : ")

for i in range(len(name)):
    character = name[i]
    char_denary = ord(character)
    binary = bin(char_denary)
    print(character, "=>", binary)
