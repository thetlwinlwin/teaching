adele_file = open('greetings.txt', 'r')


for line in adele_file.readlines():
    print(line.rstrip('\n'), 'hahaha')

adele_file.close()
