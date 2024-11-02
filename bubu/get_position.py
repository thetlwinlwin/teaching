import string
alphabet = input('The Alphabet you want to know => ').lower()
position = string.ascii_lowercase.find(alphabet)+1
print(f'The Position is {position}')