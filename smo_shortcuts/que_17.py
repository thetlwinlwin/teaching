for a in range(10):
    for b in range(10):
        if b == a:
            continue
        for c in range(10):
            if b == c or c == a:
                continue
            abc = int(str(a)+str(b)+str(c))
            cbabc = int(str(c)+str(b)+str(a)+str(b)+str(c))
            abcba = int(str(a)+str(b)+str(c)+str(b)+str(a))
            if abc % 3 == 0 and cbabc % 15 == 0 and abcba % 8 == 0:
                print(a, b, c)
