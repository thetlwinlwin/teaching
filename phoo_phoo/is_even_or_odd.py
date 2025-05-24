usr_num = input("Enter a number: ")
usr_num = int(usr_num)

is_odd = usr_num % 2 == 1
is_odd = usr_num % 2 != 0
print(type(is_odd))
print("The number entered is odd", is_odd)
