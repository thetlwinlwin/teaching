from random import random

registration = []
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def random_int(start, end):
    width = end - start + 1
    random_num = random()
    random_integer = (random_num*width)+start
    random_integer = random_integer // 1
    return int(random_integer)


for i in range(20):
    user_info = []
    first_letter_idx = random_int(0, 25)
    first_letter = letter[first_letter_idx]
    second_letter_idx = random_int(0, 25)
    second_letter = letter[second_letter_idx]
    name = first_letter + second_letter  # concatenation
    age = random_int(4, 14)
    initial_pb = 0
    initial_num_of_run = 0
    user_info.append(name)
    user_info.append(age)
    user_info.append(initial_pb)
    user_info.append(initial_num_of_run)

    registration.append(user_info)

print(registration)
