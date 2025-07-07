fact = int(input('enter number : '))
total = 1

if fact == 0:
    print(total)
elif fact < 0:
    print('invalid factorial')
else:
    for i in range(1, fact+1):
        total *= i
    print(total)
