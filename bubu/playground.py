Evening = [
    [1, 243, 35, 365],
    [1, 54, 37, 47],
    [36, 46, 357, 5],
    [35, 68, 8, 44],
    [45, 6, 879, 9, 10, 475],
]

for row_idx in range(len(Evening)):
    for seat_idx in range(20):
        print("row", row_idx, "seat", seat_idx, "is", Evening[row_idx][seat_idx])
