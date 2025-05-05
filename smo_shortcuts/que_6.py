odd = 5
p_sq = 2
total = 1

while odd<45:
    num = f'1+({odd}/{p_sq**2})'
    total *= eval(num)
    odd += 2
    p_sq += 1


print(total)
