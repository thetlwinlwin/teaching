total = 0

for i in range(2, 10):
    num = f"1/({i}*{i+1})"
    result = eval(num)
    total += result

print(total * 100)
