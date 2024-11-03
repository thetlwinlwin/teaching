# Iteration

# For
# String
username = "Vincent"
for char in username:
    result = char + char
    print(result)

print("\n")
# Int
# integer cannot be looped
user_int = 56789
# string integer can
user_int = "56789"
user_sum = 0
for i in user_int:
    user_sum = user_sum + int(i)

print(user_sum)

# Array
user_array = [12, 43645, 745, 7, 453, 645, 635]
max_val = 0
for i in user_array:
    if i > max_val:
        max_val = i
print(max_val)
