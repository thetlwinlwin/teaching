# Post-Condition Loop

total = 0
mark = 0

is_loop_ended = False

while not is_loop_ended:
    mark = int(input("Enter mark -1 to finish : "))
    total = total + mark
    if mark == -1:
        is_loop_ended = True

print("total is", total)
