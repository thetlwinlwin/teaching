name = input("Enter your name : ")

for i in range(len(name)):
    char = name[i]
    char_denary = ord(char)
    binary = bin(char_denary)
    print(char, "=>", char_denary, "=>", binary[2:])
