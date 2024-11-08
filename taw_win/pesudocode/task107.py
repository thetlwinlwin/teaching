is_done = False

words = []
print("Enter blank will end the loop")

while not is_done:
    user_input = input("Enter word : ")
    if user_input == "":
        is_done = True
    if not user_input in words:
        words.append(user_input)

for word in words:
    print(word)


"""
DECLARE Words : ARRAY OF STRING
DECLARE UserInput : STRING
DECLARE Counter, CurrentSize,ArrSize : INTEGER
Counter <- 0


OUTPUT "enter word,empty word to end"
REPEAT 
    Input UserInput
    CurrentSize <- LENGTH(Words)
    IF NOT CurrentSize = 0
        THEN
            FOR Idx <- 0 to CurrentSize - 1
                IF NOT Words[Idx] = UserInput
                    THEN
                        Words[Counter] <- UserInput
                ENDIF
            NEXT Idx
        ELSE
            Words[Idx] = UserInput
    ENDIF  
    Counter <- Counter + 1
UNTIL UserInput = ''

ArrSize <- LENGTH(Words)
FOR Counter <- 0 to ArrSize - 1
    OUTPUT Words[Counter]
NEXT Counter
"""
