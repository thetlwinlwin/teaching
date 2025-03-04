file = open("bubu.txt", "w")

is_done = False
while is_done != True:
    user_text = input('enter text(type "end" to end) : ')
    if user_text == "end":
        is_done = True
    else:
        file.write(user_text + "\n")

file.close()
