from random import randint

print('Guess the number between 1 and 100')

RAND_NUM = randint(1,100)
NUM_OF_ATTEMPT = 0

while True:
    user_guess = int(input('guess ur number : '))
    NUM_OF_ATTEMPT +=1
    if user_guess>RAND_NUM:
        print('number is too big')
    elif user_guess<RAND_NUM:
        print('number too small')
    else:
        print('yayyy. you got it')
        print(f'You got it after {NUM_OF_ATTEMPT} attempt/s')
        break
