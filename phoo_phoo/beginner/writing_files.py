file = open('noah.txt', 'w')

username = input('Enter your name: ')
age = input('Enter your age: ')
file.write(username+'\n')
file.write(age)


file.close()
