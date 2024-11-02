def find_neg_num(num_arr: list[int])->int:
    for idx in range(len(num_arr)):
        if num_arr[idx] < 0:
            return idx
    return -1


'''
FUNCTION FindNegNum(NumArr : ARRAY OF INTEGER)RETURN INTEGER
    DECLARE Index,ArraySize INTEGER
    DECLARE Found BOOLEAN
    Index <- -1
    ArraySize <- LENGTH(NumArr)
    Found <- False
    Counter <- 1
    REPEAT
        IF NumArr[Counter] < TargetVal
        THEN
            Index <- Counter
            Found <- True
        ELSE
            Counter = Counter + 1
        ENDIF
    UNTIL Found OR Counter > ArraySize
    RETURN Index
'''
