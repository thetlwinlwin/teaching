import math
n = 0

for i in range(10,100):
    reverse = int(str(i)[::-1])
    sum = i+reverse
    if math.sqrt(sum)%1 == 0:
        n += 1
        print(f'number is {i}')

print(f'total count is {n}')