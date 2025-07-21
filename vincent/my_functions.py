def count_upper_lower_chars(input_string):
    uppercase = 0
    lowercase = 0
    for char in input_string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    return [uppercase, lowercase]
