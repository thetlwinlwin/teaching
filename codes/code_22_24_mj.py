from random import random

GRID = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
]

X_row = (random() * (4 - 0)) + 0
X_row = int(round(X_row, 0))

X_col = (random() * (4 - 0)) + 0
X_col = int(round(X_col, 0))

while X_row == 0 and X_col == 0:
    X_row = (random() * (4 - 0)) + 0
    X_row = int(round(X_row, 0))

    X_col = (random() * (4 - 0)) + 0
    X_col = int(round(X_col, 0))


GRID[X_row][X_col] = "X"

current_row = 0
current_col = 0
count = 10
restart = False
is_done = False

for i in GRID:
    print(i)

while not is_done:
    direction = input("Left,Right,Up or Down : ").lower()
    if direction == "up":
        current_row -= 1
    if direction == "down":
        current_row += 1
    if direction == "right":
        current_col += 1
    elif direction == "left":
        current_col -= 1

    print(f"{current_row=}")
    print(f"{current_col=}")

    count -= 1

    if count == 0:
        is_done = True

    if current_col == X_col and current_row == X_row:
        print(f"{10-count} moves")
        is_done = True
