from random import random

any_random = random()
print(f'\noriginal random number from random() is {any_random}')
min = 3
max = 21
width = max - min + 1

random_int = (any_random * width) + min
random_int = random_int // 1


print(f'\nnow it becomes {random_int}')
