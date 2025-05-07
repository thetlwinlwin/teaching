user_input = input("enter something: ")
user_input_type = type(user_input)
print(user_input_type)

# number (eg. 12)   =>  str
# string (eg. hi)   =>  str
# bool   (eg. True) =>  str

# conclusion => every input is string

user_age = int(input("enter your age"))
user_age_type = type(user_age)
print(user_age_type)
# 1 => int
# anything other than number => Error
