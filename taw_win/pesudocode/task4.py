def is_perfect_num(val: int) -> bool:
    divisors = []
    for i in range(1, val):
        if val % i == 0:
            divisors.append(i)
    return sum(divisors) == val


print("perfect number between 1 and 10_001")
for i in range(1, 10_001):
    if is_perfect_num(i):
        print(i)

"""
FUNCTION IsPerfectNum(Value : INTEGER) RETURN BOOLEAN
    DECLARE DivisorSum, CurrentDivisor : INTEGER
    DivisorSum <- 0
    FOR I <- 1 TO Value - 1
        CurrentDivisor <- MOD(Value,I)
        IF CurrentDivisor = 0
            THEN
                DivisorSum = DivisorSum + I
        ENDIF
    NEXT I
    RETURN DivisorSum = Value

OUTPUT "Perfect Number between 1 and 10,000"
DECLARE IsValuePerfect : BOOLEAN

FOR II <- 1 to 10000
    IsValuePerfect <- IsPerfectNum(II)
    IF IsValuePerfect
        THEN
            OUTPUT II
    ENDIF
NEXT II
"""
