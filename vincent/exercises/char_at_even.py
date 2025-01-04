print(
    """
    Enter a word.
    I will show you chars at even index.
"""
)

user_input = input("Enter a word : ")

for i in range(len(user_input)):
    if i % 2 == 0:
        print(user_input[i])
