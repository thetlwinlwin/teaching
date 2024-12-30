word = input("Enter the word : ")
char_count = len(word)

is_parlindrome = True

for i in range(char_count):
    if word[i] != word[-i - 1]:
        is_parlindrome = False
        break

if is_parlindrome == True:
    print("It is parlindrome")
else:
    print("It's not.")
