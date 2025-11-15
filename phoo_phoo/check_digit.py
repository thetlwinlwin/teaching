for i in range(21):
    str_i = str(i)
    if len(str_i) == 1:
        x = '00'+str_i
    else:
        x = '0'+str_i

    # start here
    count = 4
    total = 0
    for digit in x:
        total = total + int(digit)*count
        count = count - 1

    remainder = (total % 11)
    check_digit = 11 - remainder
    if check_digit == 10:
        x = x + 'x'
    elif check_digit == 11:
        x = x + '0'
    else:
        x = x + str(check_digit)
    print(x)
