usr_in = input("Enter your number : ")
multiply_by = len(usr_in) + 1
total = 0

for i in usr_in:  # i <- str
    result = int(i) * multiply_by
    multiply_by = multiply_by - 1
    total = total + result

remainder = total % 11

if remainder == 10:
    last_val = "X"
elif remainder == 0:
    last_val = remainder
else:
    last_val = 11 - remainder

print("\n Your number is", usr_in + str(last_val))
