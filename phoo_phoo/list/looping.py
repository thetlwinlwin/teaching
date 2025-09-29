marks = [10, 8, 14, 10, 9, 11]
output = []

# # count all the even marks
# # python style
# for element in marks:
#     print(element)

# generic style
for idx in range(len(marks)):
    output[idx] = marks[idx] ** 2
