from random import random

# between 11 and 25
# x = random()*(largest-smallest) + smallest

x = (random() * (25 - 11)) + 11
print(round(x, 0))
