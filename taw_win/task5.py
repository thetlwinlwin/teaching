def word_recognition(text: str) -> list[str]:
    words = text.split(" ")
    result = []
    for word in words:
        result.append(word.strip("':;?!.-,"))
    return result


print(word_recognition("Examples of contractions include: don't, isn't, and wouldn't."))


"""
DECLARE UserInput, Word, CurrentWord : STRING
DECLARE Counter, Start, End : INTEGER
DECLARE WordList, Result : ARRAY OF STRING
punctuation = [",", ".", "?", "-", "!", "'", ":", ";"]


Counter <- 0
Word <- ""

OUTPUT "Enter your text : "
INPUT UserInput

FOR Idx <- 0 to LENGTH(UserInput) - 1
    IF NOT UserInput[Idx] = " "
        THEN
            Word <- Word + UserInput[Idx]
        ELSE
            WordList[Counter] <- Word
            Word <- ""
            Counter <- Counter + 1
    ENDIF
NEXT Idx

FOR Idx <- 0 to Counter
    CurrentWord <- WordList[Idx]
    Start <- 
NEXT Idx


"""
