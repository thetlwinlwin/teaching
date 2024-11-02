age = int(input("Age : "))
born_in_us = input("Born in US (Y/N) :").lower()
residency = int(input("How long do you live in US : "))

is_native = born_in_us == "y"


if age >= 35 and is_native and residency >= 14:
    print("You are eligible to run for president.")
else:
    print("You are not eligible to run for president")

if age < 35:
    print("You are too young. You must be at least 35 years old.")

if not is_native:
    print("You must be born in the U.S. to run for president.")

if residency < 14:
    print("You have not been a resident for long enough.")
