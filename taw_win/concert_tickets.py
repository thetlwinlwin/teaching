buy = True
total = 0

while buy == True:
    num_of_tickets = int(input("Enter ticket numbers : "))
    if num_of_tickets > 25:
        print("You cannot buy that much at once.")
    elif num_of_tickets >= 20:
        price = (num_of_tickets*20)-(num_of_tickets*20*0.2)
        print(price)
        total = total + price
    elif num_of_tickets >= 10:
        price = (num_of_tickets*20)-(num_of_tickets*20*0.1)
        print(price)
        total = total + price
    else:
        total = total + (num_of_tickets * 20)

    status = input("wanna buy more Y/N : ")
    buy = status == "Y"


print("total is :", total)
