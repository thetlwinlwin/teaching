file = open('names.txt', 'r')  # r means read

# file.read()       -> read each word
# file.readline()   -> read the first line
# file.readlines()  -> read line by line

# strip() remove {\n} from the line "Vincent{\n}"

name_list = []
for line in file.readlines():
    line = line.strip()
    name_list.append(line.upper())

file.close()

another_file = open('name_upper.txt', 'w')

for name in name_list:
    another_file.write(name+'\n')

another_file.close()
