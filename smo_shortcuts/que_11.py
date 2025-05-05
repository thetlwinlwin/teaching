import math as m

n = 8
total = m.factorial(3)*m.factorial(5)*m.factorial(7)
while m.factorial(n)!=total:
    n+=1

print(f'n is {n}')