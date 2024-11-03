def count_occurance(num_arr: list[int], target: int) -> int:
    count = 0
    for element in num_arr:
        if element == target:
            count += 1
    return count


"""
FUNCTION CountOccurance(NumArr : ARRAY OF INTEGER, Target: INTEGER) RETURN INTEGER
    DECLARE Count,ArrSize INTEGER
    Count <- 0
    ArrSize <- LENGTH(NumArr)
    FOR Counter <- 0 TO ArrSize
        IF NumArr[Counter] = Target:
            THEN
                Count <- Count + 1
        ENDIF
    
    RETURN Count
"""
