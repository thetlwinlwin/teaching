# THIS SHOULD NOT BE IN HOMEWORK.
# THIS IS FAMOUS ALGORITHM AND WORTH TEACHING

def bi_search(sorted_arr:list[int],target: int)->int:
    left = 0
    right = len(sorted_arr)-1

    while left <= right:
        mid = left+(right-left)//2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


'''
FUNCTION BiSearch(SortedArr : ARRAY OF INTEGER, Target: INTEGER)RETURN INTEGER
    DECLARE Left,Right,Index INTEGER
    DECLARE Found BOOLEAN
    Left <- 0
    Right <- LENGTH(SortedArr)
    Index <- -1
    Found <- False

    REPEAT
        Mid <- Left + DIV(Right - Left,2)
        IF SortedArr[Mid] == Target
            THEN
                Index <- Mid
                Found <- True
            ELSE
                IF SortedArr[Mid] < Target
                    THEN
                        Left = Mid + 1
                    ELSE
                        Right = Mid - 1
                ENDIF
        ENDIF
    UNTIL Found OR Left>Right 
    RETURN Index   
'''