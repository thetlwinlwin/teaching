total = 0
for i in range(100,0,-1):
    print(i)
    if i%2 == 0:
        total += i**2
    else:
        total -= i**2

print(f'total is {total}')

