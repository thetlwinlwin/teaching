total = 0
for i in range(1,10):
    n = 2*i
    num = f'1/({n}*{n+2})'
    result = eval(num)
    total += result

print(f'result is {total*100}')
