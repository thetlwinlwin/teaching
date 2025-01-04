print(
    """
    remove first "n" number of letters from a string.
"""
)


user_input = input("Enter a sentence : ")
num_of_removal = int(input("How many letters you want to remove? : "))

print("\nThere you Go!\n")
print(user_input[num_of_removal:])
