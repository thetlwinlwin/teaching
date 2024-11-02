username = input('What is your name : ')
gender = input('Your Gender (M/F) : ').lower()

result = 'Mr.'+username if gender == 'm' else 'Miss '+username

print(f'Hello! {result}!')

