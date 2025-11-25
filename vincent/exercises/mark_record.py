mark_input = int(input('Enter marks (-1 to save): '))
marks = []

while mark_input != -1:
    marks.append(mark_input)
    mark_input = int(input('Enter marks (-1 to save): '))

print('Saving Now...')

file = open('mark_records.txt', 'w')

for mark in marks:
    file.write(str(mark)+'\n')


file.close()
print('Done Saving')
