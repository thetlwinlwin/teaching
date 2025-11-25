import pprint
from random import random

ids = []
ages = []
names = [
    "James",
    "Olivia",
    "William",
    "Charlotte",
    "Benjamin",
    "Amelia",
    "Henry",
    "Harper",
    "Alexander",
    "Grace",
    "Samuel",
    "Emma",
    "Daniel",
    "Lily",
    "Thomas",
    "Chloe",
    "Nathan",
    "Sophie",
    "Jack",
    "Ella"
]
pb_times = []
num_of_runs = []


def random_int(start, end):
    width = end - start + 1
    random_num = random()
    random_integer = (random_num*width)+start
    random_integer = random_integer // 1
    return int(random_integer)


for i in range(20):
    # unique id
    str_i = str(i)
    if len(str_i) == 1:
        user_id = '00'+str_i
    else:
        user_id = '0'+str_i
    count = 4
    total = 0
    for digit in user_id:
        total = total + int(digit)*count
        count = count - 1

    remainder = (total % 11)
    check_digit = 11 - remainder
    if check_digit == 10:
        user_id = user_id + 'x'
    elif check_digit == 11:
        user_id = user_id + '0'
    else:
        user_id = user_id + str(check_digit)
    ids.append(user_id)

    # age
    user_age = random_int(4, 14)
    ages.append(user_age)

    # PB time
    pb_times.append(0)

    # num of runs
    num_of_runs.append(0)
