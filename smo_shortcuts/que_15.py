for i in range(1000,10000):
    a,b,c,d = [int(j) for j in str(i)]
    if i+a+b+c+d == 8888:
        print(f'result is {i}')
        break