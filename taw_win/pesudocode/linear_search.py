def linear_search(num_arr : list[int],target_val: int)-> int:
    for idx in range(len(num_arr)):
        if num_arr[idx] == target_val:
            return idx
    return -1


'''
Version 1

FUNCTION LinearSearch(NumArr : ARRAY OF INTEGER, TargetVal : INTEGER) RETURN INTEGER
    FOR Idx <- 1 TO LENGTH(NumArr)
       IF NumArr[Idx] == TargetVal
            THEN
                RETURN Idx
        ENDIF
    NEXT
    RETURN -1
'''


'''
Version 2

FUNCTION LinearSearch(NumArr : ARRAY OF INTEGER, TargetVal : INTEGER) RETURN INTEGER
    DECLARE Index,ArraySize INTEGER
    DECLARE Found BOOLEAN
    Index <- -1
    ArraySize <- LENGTH(NumArr)
    Found <- False
    Counter <- 1
    REPEAT
        IF NumArr[Counter] == TargetVal
        THEN
            Index <- Counter
            Found <- True
        ELSE
            Counter = Counter + 1
        ENDIF
    UNTIL Found OR Counter > ArraySize
    RETURN Index
'''



