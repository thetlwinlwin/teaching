que = 5
table = 2
retest = True
while retest:
    right = 0
    for que_num in range(1,que+1):
        print('Question Number ',que_num)
        print(table,'x',que_num)
        ans = int(input("Ur Ans : "))
        if ans == (table*que_num):
            print('You are right!')
            right+=1
        else:
            print('You are wrg.')
    print('The test is over and you got ', right,' marks.')
    choice = input('Wanna retake y/n : ').lower()
    if choice == 'y':
        retest = True
    else:
        retest = False


