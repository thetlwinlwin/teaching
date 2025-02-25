user_list = []

is_done = False

while not is_done:
    usr_input = input('Enter Number(type "end" to end) : ')
    if usr_input == "end":
        is_done = True
    else:
        user_list.append(int(usr_input))

total = len(user_list)

for loop in range(total - 1):
    print("loop", loop)
    for i in range(total - loop - 1):
        ele_at_i = user_list[i]
        ele_at_i_1 = user_list[i + 1]
        if ele_at_i > ele_at_i_1:
            user_list[i + 1] = ele_at_i
            user_list[i] = ele_at_i_1

print(user_list)
