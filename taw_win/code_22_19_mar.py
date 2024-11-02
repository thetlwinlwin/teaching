STUDENT_DATA = []

SUBJECTS = ['phy','chem','his','geo','cs']

# have to use while loop
for _ in range(3):
    name = input('Name : ')
    choice = input('Subject Choice : ').lower()
    if choice not in SUBJECTS:
        print('Invalid choice')
        continue
    STUDENT_DATA.append([name,choice])

print(STUDENT_DATA)