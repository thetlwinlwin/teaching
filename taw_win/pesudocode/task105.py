int_list = []

is_done = False
print('End the loop by entering "0"')

while not is_done:
    user_input = int(input("Enter Integer : "))
    int_list.append(user_input)
    if user_input == 0:
        is_done = True
    else:
        int_list.append(user_input)

for idx in range(len(int_list) - 1, -1, -1):
    print(int_list[idx])


"""
DECLARE IntList : ARRAY OF INTEGER
DECLARE UserInt,Counter,ArrSize : INTEGER
Counter <- 0

OUTPUT "Enter Integer,0 to finish "

REPEAT
    INPUT UserInt
    IF NOT UserInt = 0
        THEN
            IntList[Counter] <- UserInt
    ENDIF
    Counter <- Counter + 1
UNTIL UserInt = 0

REPEAT
    OUTPUT IntList[Counter]
    Counter <- Counter - 1
UNTIL Counter = -1
"""
