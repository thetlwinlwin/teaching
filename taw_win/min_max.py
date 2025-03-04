marks = [7, 75, 80, 60, 70, 65, 75, 25, 95, 100]

max_mark = marks[0]
min_mark = marks[0]
class_size = len(marks)

for i in marks:
    if i > max_mark:
        max_mark = i
    elif i < min_mark:
        min_mark = i

print("max mark", max_mark)
print("min mark", min_mark)
