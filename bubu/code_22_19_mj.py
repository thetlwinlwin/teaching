ITEM_NUMBER = [i for i in range(10)]
ITEM_DESCRIPTION = ["Item "+str(i) for i in range(10)]
RESERVE_PRICE = [3706, 6119, 4209, 8104, 332, 6648, 1502, 7086, 4772, 4744]
num_of_bid  = [0 for _ in range(10)]

cur_highest_price = [3706, 6119, 4209, 8104, 332, 6648, 1502, 7086, 4772, 4744]
highest_price_by = [None for _ in range(10)]

print('WELCOME')

for _ in range(3):
    # ask Item Number
    item_num = int(input("Search Item by ID : "))

    # Print out the item data
    print("*"*50)
    print('Item Number : '+str(item_num))
    print('Description : '+ITEM_DESCRIPTION[item_num])
    print('Current Highest : '+str(cur_highest_price[item_num]))
    print("*"*50)

    # bidding
    buyer_num = int(input('Enter your number : '))
    bid_amount = float(input('Enter the amount you want to bid : '))

    while bid_amount < cur_highest_price[item_num]:
        print('too low')
        bid_amount = float(input('Enter the amount you want to bid : '))

    cur_highest_price[item_num] = bid_amount
    highest_price_by[item_num] = buyer_num

    print('current highest price')
    print(cur_highest_price)
    print('highest price by')
    print(highest_price_by)
    



