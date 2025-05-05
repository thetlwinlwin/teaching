# denary => binary
denary_input = input("Enter denary number: ")
denary_input = int(denary_input)

binary_num = bin(denary_input)
print(binary_num)


# denary => hexadecimal
denary_input = input("Enter denary number: ")
denary_input = int(denary_input)

hex_num = hex(denary_input)
print(hex_num)


# binary => denary
binary_input = input("Enter binary number: ")

denary_num = int(binary_input, 2)
print(denary_num)


# binary => hexadecimal
binary_input = input("Enter binary number: ")

denary_num = int(binary_input, 2)
hex_num = hex(denary_num)
print(hex_num)


# hexadecimal => binary
hex_input = input("Enter hexadecimal number: ")

denary_num = int(hex_input, 16)
binary_num = bin(denary_num)
print(binary_num)


# hexadecimal => denary
hex_input = input("Enter hexadecimal number: ")

denary_num = int(hex_input, 16)
print(denary_num)
