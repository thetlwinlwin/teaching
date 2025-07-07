todo_list = []
is_done = False

while is_done == False:
    todo = input('enter todo ("done" to stop): ')
    if todo.lower() == "done":
        is_done = True
    else:
        if todo not in todo_list:
            todo_list.append(todo.capitalize())
