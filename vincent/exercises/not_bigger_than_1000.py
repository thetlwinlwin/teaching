print("Welcome\n")
print(
    """
    This program will return the product of two numbers
    only if it is less than 1000.
    Otherwise, the sum of two numbers will be returned.
"""
)

first_num = int(input("Enter first number : "))
second_num = int(input("Enter second number : "))

product = first_num * second_num

print("\nThe Result is\n")

if product > 1000:
    print(first_num + second_num)
else:
    print(product)
