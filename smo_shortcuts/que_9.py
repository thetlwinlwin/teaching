is_done = False

for num in range(1000,10000):
    num_list = [i for i in str(num)]
    b = num_list[1]

    for sec in range(100,1000):
        the_list = num_list + [i for i in str(sec)]
   
        if len(set(the_list)) == len(the_list):
            a,b,c,d = [i for i in the_list[0:4]]
            e,f,g = [i for i in the_list[4:]]
            total = eval(f'{a+b+c+d}+{e+f+g+b}')

            if total < 10000:
                continue

            result = [i for i in str(total)]
            h = result[4]
            if h in the_list:
                continue

            if result[0]==e and result[1]==f and result[2]==c and result[3]==b:
                print('found it')
                print(f'a => {a}\nb => {b}\nc => {c}\nd => {d}\ne => {e}\nf => {f}\ng => {g}\nh => {h}')
                is_done = True
                break
            
    if is_done:
        break


