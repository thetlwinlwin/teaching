def linear_search(array, target_val):
    for i in range(len(array)):
        if array[i] == target_val:
            return i
    return -1


x = linear_search(
    array=[1, 3, 4, 6, 64],
    target_val=7,
)
print(x)

y = linear_search(
    array=[3, 56, 64, 235, 64, 64],
    target_val=64,
)
print(y)
