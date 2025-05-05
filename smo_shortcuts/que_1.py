total = 0 
for i in range(99):
    num = '9'*(i+1)
    total += int(num)

result = str(total).count('1')
print(result)