ITEM_NUMBER = [i for i in range(10)]
ITEM_DESCRIPTION = ["Item " + str(i) for i in range(10)]
RESERVE_PRICE = [3706, 6119, 4209, 8104, 332, 6648, 1502, 7086, 4772, 4744]
num_of_bids = [0 for _ in range(10)]

cur_highest_price = [0 for _ in range(10)]
is_sold = [False for _ in range(10)]
num_of_item_sold = 0

is_auction_end = False
print("WELCOME")

while not is_auction_end:
    # ask Item Number
    item_num = input("Search Item by ID (press q to quit) : ")
    if item_num == "q" or item_num == "Q":
        is_auction_end = True
    else:
        item_num = int(item_num)
        if is_sold[item_num]:
            print("*" * 50)
            print("That item", item_num, "is sold out!")
            print("*" * 50)
        else:
            # Print out the item data
            print("*" * 50)
            print("Item Number : " + str(item_num))
            print("Description : " + ITEM_DESCRIPTION[item_num])
            print("Current Highest : " + str(cur_highest_price[item_num]))
            print("Number of Bids :", num_of_bids[item_num])
            print("*" * 50)

            # bidding
            buyer_num = int(input("Enter your Buyer number : "))
            bid_amount = float(input("Enter the amount you want to bid : "))

            while bid_amount < cur_highest_price[item_num]:
                print("too low")
                bid_amount = float(input("Enter the amount you want to bid : "))

            cur_highest_price[item_num] = bid_amount  # type: ignore
            num_of_bids[item_num] += 1

            if bid_amount >= RESERVE_PRICE[item_num]:
                is_sold[item_num] = True
                num_of_item_sold += 1
                print("\n", "*" * 50)
                print("Congrat!")
                print("Sold to", buyer_num, "by amount of", bid_amount * 1.1)
                print("\n", "*" * 50)
    print("current highest is ", cur_highest_price)
    print("\n\n")

num_of_items_not_meeting_price = 0
num_of_items_not_bid_once = 0
for item_num in ITEM_NUMBER:
    if is_sold[item_num] == False:
        print("Item", item_num, "got", cur_highest_price[item_num])
        num_of_items_not_meeting_price += 1

print("\n")
for item_num in ITEM_NUMBER:
    if num_of_bids[item_num] == 0:
        print("Item", item_num, "received no bidding")
        num_of_items_not_bid_once += 1

print("\n")
print("total item sold", num_of_item_sold)
print("Num of Item not meeting the price", num_of_items_not_meeting_price)
print("Num of Item not bid once", num_of_items_not_bid_once)
