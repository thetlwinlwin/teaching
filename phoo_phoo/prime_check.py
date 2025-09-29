def prime_checker(num):
    '''
    num > 2.
    This function will print out whethere the given input is prime or not.
    '''
    is_prime = True
    for i in range(2, num//2):
        if num % i == 0:
            is_prime = False

    if is_prime == True:
        print('It is a prime number')
    else:
        print('It is not a prime number')
