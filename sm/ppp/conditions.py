mark = input('Gimme your damn mark(1-100): ')
mark = float(mark)

if mark > 100 or mark < 0:
    print('Fuck off!')
else:
    print('It is in the range')
    if mark < 40:
        print('F')
    elif mark < 50:
        print('D')
    elif mark < 60:
        print('C')
    elif mark < 75:
        print('B')
    else:
        print('A')


print('program end')
