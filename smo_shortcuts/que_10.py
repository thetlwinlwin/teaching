import math as m

total = 0

for i in range(1,101):
    total += m.factorial(i)

unit_digit = total%10

print(f'unit digit is {unit_digit}')