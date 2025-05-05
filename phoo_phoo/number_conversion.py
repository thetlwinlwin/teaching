# denary => binary
denary_input = input("Enter denary number: ")
denary_input = int(denary_input)

binary_num = bin(denary_input)
print(binary_num)


# binary => denary
binary_input = input("Enter binary number: ")

denary_num = int(binary_input, 2)
print(denary_num)
