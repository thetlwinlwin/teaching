for i in range(100,1000):
    a,b,c = [int(j) for j in str(i)]
    if 49*a + 7*b + c == 286:
        print(f'result is {i}')
        break