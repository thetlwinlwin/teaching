mark_list = [
    [1, 100, 100, 100],
    [2, 50, 49, 68],
    [3, 73, 99, 63],
]

for row_num in range(len(mark_list)):
    if row_num == 1 or row_num == 2:
        row = mark_list[row_num]
        print(row[1])
