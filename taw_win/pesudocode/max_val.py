def max_val(num_arr:list[int])->int:
    max_num = num_arr[0]
    if len(num_arr) == 1:
        return max_num
    for element in num_arr:
        if element > max_num:
            max_num = element
    return max_num

'''
FUNCTION MaxVal (NumArr : ARRAY OF INTEGER) RETURN INTEGER
    DECLARE MaxNum,ArrSize INTEGER
    MaxNum <- NumArr[1]
    ArrSize <- LENGTH(NumArr)
    IF ArrSize == 1:
        THEN
            RETURN MaxNum
    ENDIF
    FOR Counter <- 2 TO ArrSize:
        IF NumArr[Counter]> MaxNum
            THEN
                MaxNum <- NumArr[Counter]
        ENDIF
    NEXT Counter
    RETURN MaxNum
'''