total = 0
n = 1
count = 0

while True:
    sub_total = 0
    for i in range(n):
        fraction = f'{i+1}/{n}'
        sub_total += eval(fraction)
        count += 1
        if count == 1000:
            break
    total += sub_total
    if count == 1000:
        break
    else:
        n+=1


print(total)
