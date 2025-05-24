# 1. if it has one float dtype, the result would be in float dtype.
# 2. division => result is alway float dtype.
# 3. obeys the orders of operation
import math

# integer
addition = 1 + 1
print(addition)
subtraction = 5 - 11
print(subtraction)
# the result is float dtype
division = 50 / 10
print(division)

# fraction
addition = 1 / 2 + 1 / 3
print(addition)
subtraction = 1 / 3 - 1 / 2
print(subtraction)
division = 3 / 4 * 2
print(division)

# decimal => float
addition = 1 + 1.0
print(addition)
subtraction = 13.9 - 0.9
print(subtraction)

# square root
result = math.sqrt(2)
print(result)


# multiplication
multiply = 5 * -2.0
print(multiply)

# power
power = (3 / 2) ** -2
power1 = 3 / 2**-2
# power1 is not equal to power
print(power)

# integer division // floor division
# given out the whole number part of the quotient
# 5.66 => 5, 5.33 => 5
int_division = 17 // 3
print(int_division)


# remainder
remainder = 17 % 3
print(remainder)
