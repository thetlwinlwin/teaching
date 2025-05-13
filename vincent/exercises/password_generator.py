import random
import string

length = int(input("Enter the password length : "))

while length < 8:
    print("Password should be at least 6 characters long.")
    length = int(input("Enter the password length : "))

password = ""

for _ in range(length):
    char_list = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]
    pick = random.choice(char_list)
    char = random.choice(pick)
    password += char

print("Your password is :", password)
