tali = {
    "i": 1,
    "v": 5,
    "x": 10,
}


user_input = input("Enter Roman letter: ")

total = 0
for i in range(len(user_input) - 1):
    current = user_input[i]
    if user_input[i + 1]:
        right = user_input[i + 1]
        if tali[right] > tali[current]:
            total -= tali[current]
        else:
            total += tali[current]
total += tali[user_input[-1]]

print(total)
