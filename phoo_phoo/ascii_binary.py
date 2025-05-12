user_input = input("Enter a character: ")

ascii_num = ord(user_input)
binary_num = bin(ascii_num)

print("Ascii number of", user_input, "is", ascii_num)
print("Binary value of that ASCII char is", binary_num)
