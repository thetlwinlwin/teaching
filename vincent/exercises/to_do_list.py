to_do_list = []

is_finished = False

while not is_finished:
    to_do = input("Enter (type 'done' to stop) : ").capitalize()
    if to_do == "Done":
        is_finished = True
    elif to_do not in to_do_list:
        to_do_list.append(to_do)

print("The list is as follow")
print(to_do_list)
