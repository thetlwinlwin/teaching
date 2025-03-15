is_done = False

while not is_done:
    num_1 = int(input("Num 1 : "))
    num_2 = int(input("Num 2 : "))
    if num_1 * num_2 > 100:
        print("Product is greater than 100")
    more = input("wanna test more Y/N : ")
    if more != "Y":
        is_done = True
