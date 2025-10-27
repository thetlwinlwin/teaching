from random import random

menu_items = ["French fries", "1/4 pound burger",
              "1/4 pound cheeseburger",
              "1/2 pound burger",
              "1/2 pound cheeseburger",
              "Medium pizza",
              "Medium pizza with extra toppings",
              "Large pizza",
              "Large pizza with extra toppings",
              "Garlic bread"
              ]

prices = [
    2.00,
    5.00,
    5.55,
    7.00,
    7.50,
    9.00,
    11.00,
    12.00,
    14.50,
    4.50,
]
menu_item_codes = [
    "M01",
    "M02",
    "M03",
    "M04",
    "M05",
    "M06",
    "M07",
    "M08",
    "M09",
    "M10",
]

order_ids = []
daily_sales = []
is_new_order = True

while is_new_order:
    print('\n\nWELCOME\n\n')
    print('Here are our menu items\n')
    for i in range(10):
        print(menu_item_codes[i], '\t',
              f'{menu_items[i]:<40}', f'{prices[i]:>4}')

    print('\n')
    is_order_done = False
    item_codes = []
    serving_amounts = []

    while not is_order_done:
        order_code = input('Enter item code: ')
        order_amount = input('How many serving: ')
        add_another_order = input('Add another item Y/N: ').lower()
        if add_another_order == 'n':
            is_order_done = True
        item_codes.append(order_code)
        serving_amounts.append(order_amount)

    print('\nGood! your order is ')

    order_id = int(random()*(10**16))
    while order_id in order_ids:
        order_id = int(random()*(10**16))

    order_ids.append(order_id)

    total = 0
    for i in range(len(item_codes)):
        code = item_codes[i]
        serving = serving_amounts[i]
        serving = int(serving)
        code_position = menu_item_codes.index(code)
        item_name = menu_items[code_position]
        item_price = prices[code_position]
        total = total + (item_price*serving)
        print(item_name, 'x', serving, item_price*serving)

    daily_sales.append(total)

    print('\nYour order ID is', order_id)
    print('Your total is', total)

    new_order = input('\nNew Order?(y/n): ').lower()
    if new_order == 'y':
        is_new_order = True
    else:
        is_new_order = False

total_sales = 0
for sale in daily_sales:
    total_sales = total_sales + sale

profit = 10
print('\n Daily Sales')
print('Total is ', total_sales)
print('Profit Percentage is', profit, '%')
print('Profit is ', total_sales*profit/100)
