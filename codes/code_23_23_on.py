import random

TEMPERATURES = [
    [43, 35, 39, 32, 30, 34, 35],
    [35, 32, 48, 43, 32, 30, 45],
    [42, 31, 31, 40, 31, 40, 38],
    [41, 42, 40, 39, 39, 32, 45],
    [46, 35, 33, 33, 47, 32, 48],
    [40, 30, 42, 32, 35, 47, 38],
    [45, 48, 43, 41, 42, 38, 46],
    [43, 31, 36, 30, 39, 41, 35],
    [40, 45, 37, 37, 30, 47, 35],
    [44, 40, 45, 33, 38, 44, 41],
    [44, 45, 35, 45, 37, 30, 31],
    [30, 36, 44, 35, 47, 45, 32],
    [24, 29, 22, 38, 29, 25, 33],
    [35, 31, 25, 21, 26, 35, 20],
    [25, 36, 29, 25, 33, 36, 26],
    [27, 31, 27, 26, 29, 26, 34],
    [32, 28, 34, 27, 21, 38, 31],
    [29, 35, 23, 22, 33, 29, 27],
    [22, 24, 23, 23, 38, 24, 28],
    [34, 20, 29, 37, 37, 35, 25],
    [37, 34, 20, 32, 22, 38, 22],
    [21, 22, 25, 26, 23, 21, 24],
    [33, 34, 34, 32, 25, 36, 32],
    [29, 27, 36, 38, 31, 24, 28],
]

# No Need
# for i in range(24):
#     my_list = []
#     for j in range(7):
#         my_list.append(random.randint(30 - (i // 12) * 10, 48 - (i // 12) * 10))
#     TEMPERATURES.append(my_list)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(7):
    each_day = []
    for hour in range(24):
        each_day.append(TEMPERATURES[hour][day])
    print("For", days[day])
    print("Minimum Temperature is", min(each_day))
    print("Maximum Temperature is", max(each_day))
    print("Average Temperature is", round(sum(each_day) / 24, 2))


flatten_tempts = [temp for hour in TEMPERATURES for temp in hour]

MAX_WEEK = max(flatten_tempts)
MIN_WEEK = min(flatten_tempts)
AVG_WEEK = round(sum(flatten_tempts) / (24 * 7), 2)
print("\nFor the week")
print("Minimum Temperature is", MAX_WEEK)
print("Maximum Temperature is", MIN_WEEK)
print("Average Temperature is", AVG_WEEK)
