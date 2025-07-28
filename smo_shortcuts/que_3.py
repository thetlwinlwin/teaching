largest = int(input('enter your largest : '))
total3 = 0


for i in range(1, largest+1):
    num3 = i/(i+1)
    total3 = total3 + num3

total1 = total3 - (largest/(largest+1))
total2 = total3 - 1/2
total4 = (total3 - 1/2) - (largest/(largest+1))

result = 777*((total1*total2)-(total3*total4))
print(int(result))
