int_list = []

is_done = False
print('End the loop by entering "0"')

while not is_done:
    user_input = int(input("Enter Integer : "))
    if user_input == 0:
        is_done = True
    else:
        int_list.append(user_input)


int_list.sort()

for i in int_list:
    print(i)


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

ArrSize <- LENGTH(IntList)
First <- 0
Last <- ArrSize - 1

REPEAT
    Swap <- FALSE
    FOR Index <- First TO Last - 1
        IF IntList[Index] > IntList[Index + 1]
            THEN
                MyInt <- IntList[Index]
                IntList[Index] <- IntList[Index + 1]
                IntList[Index + 1] <- MyInt
                Swap <- TRUE
        ENDIF
    NEXT Index
    Last <- Last - 1
UNTIL (NOT Swap) OR Last = 0


FOR Counter <- 0 to ArrSize - 1
    OUTPUT IntList[0]
NEXT Counter
"""
