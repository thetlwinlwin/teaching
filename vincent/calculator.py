def menu():
    print("Vincent Program")
    print("You have 5 Options")
    print("Option 1 -> add")
    print("Option 2 -> subtract")
    print("Option 3 -> multiply")
    print("Option 4 -> divide")
    print("Option 5 -> quit")


def addition(first_num, second_num):
    return first_num + second_num


def subtraction(first_num, second_num):
    return first_num - second_num


def multiplication(first_num, second_num):
    return first_num * second_num


def division(first_num, second_num):
    return first_num / second_num


menu()

is_running = True

while is_running:
    user_option = int(input("What is your option : "))
    if user_option == 5:
        is_running = False
    else:
        first_num = int(input("Enter ur first num : "))
        second_num = int(input("Enter ur second num : "))
        if user_option == 1:
            print(addition(first_num, second_num))
        elif user_option == 2:
            print(subtraction(first_num, second_num))
        elif user_option == 3:
            print(multiplication(first_num, second_num))
        elif user_option == 4:
            print(division(first_num, second_num))


print("You quit the program")
