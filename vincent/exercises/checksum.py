x = "86 105 110 99 101 110 116 32 105 115 32 110 111 111 98"
x_list = x.split(" ")


message = ''

for val in x_list:
    val = int(val)
    message = message + chr(val)

print(message)
