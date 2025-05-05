import math
total = 0
n = 1

while True: 
    result = int(math.sqrt(n))
    total += result
    if total == 100:
        break
    else:
        n += 1

print(n)

