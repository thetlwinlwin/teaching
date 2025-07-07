marks = [10, 8, 14, 10, 9, 11, 3, 3, 9, 2, 10, 5, 6, 18, 7, 20, 5, 1, 7, 12]

# count all the even marks
# python style
count = 0
for element in marks:
    if element % 2 == 0:
        count = count + 1
print(count)

# generic style
count = 0
for idx in range(len(marks)):
    element = marks[idx]
    if element % 2 == 0:
        count = count + 1
print(count)
