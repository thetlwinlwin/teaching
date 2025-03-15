# 4 b (ii)
print('question 4')
is_same = False

while is_same != True:
    measurement = input('Enter measurement : ')
    measure_check = input('Enter Again : ')
    if measure_check == measurement:
        is_same = True


# 7
print('\nquestion 7')
flag = False
while flag != True:
    total = 0
    number = [0, 0, 0, 0, 0]
    for counter in range(0,4):
        input_digit = int(input('Enter a digit : '))
        number[counter] = input_digit
        total = total + input_digit * (counter+1)
        if number[counter] == -1:
            flag = True
    if not flag:
        number[4] = total % 10
        for value in number:
            print(value)
        print('another run')
    
    




