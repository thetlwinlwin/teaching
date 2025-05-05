left_val = 325**2
right_val = 324**2
a = 1
b = 1

while True:
    left_total = left_val + b**2
    right_total = right_val + a**2
 
    if right_total< left_total:
        a += 1
    elif right_total == left_total and a != 325 and b != 324:
        break
    else:
        b+=1

print(f'a is {a}\nb is {b}')
         



    