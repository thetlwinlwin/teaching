print("Welcome\n")
print(
    """
    looping first 10 numbers,and each loop
    print the sum of current number and previous number
"""
)


for i in range(10):
    print(
        "current number is",
        i,
        "previous number is",
        i - 1 if i != 0 else 0,
        "and the sum is",
        i + i - 1 if i != 0 else 0,
        "\n",
    )
