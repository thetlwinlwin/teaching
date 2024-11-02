# exe 1 (reverse the array)
# Given list1 = [100,200,400,800]
# Output [800,400,200,100]

list1 = [100,200,400,800]


for idx in range(4):
    new_idx = -idx-1
    print(list1[new_idx])


# 0 => -1   (-0-1)
# 1 => -2   (-1-1)
# 2 => -3   (-2-1)
# 3 => -4   (-3-1)