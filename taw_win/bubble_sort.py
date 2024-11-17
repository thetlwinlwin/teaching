temperature = [46, 7, 65, -3, 38]

first = 0  # smallest index
last = len(temperature) - 1  # largest index => 4

print("temperatue list before sorting", temperature)
while last != 0:
    for idx in range(first, last):
        if temperature[idx] > temperature[idx + 1]:
            temp = temperature[idx]
            temperature[idx] = temperature[idx + 1]
            temperature[idx + 1] = temp
    last = last - 1


print("temperature list is now", temperature)

"""Version 2"""
temperature.sort()
print("temperature is now", temperature)
