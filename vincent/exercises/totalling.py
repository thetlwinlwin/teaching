total = 0
is_done = False

while not is_done:
    user_input = input('Enter Number (type "end" to end): ')
    if user_input == "end":
        is_done = True
    elif not user_input.isnumeric() and not user_input.startswith("-"):
        print("Sir, Calm your fuck down and type number.")
    else:
        total += int(user_input)


print(total)
