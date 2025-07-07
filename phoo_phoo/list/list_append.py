mark_list = []
mark = int(input('Enter ur marks : '))
while mark != -1:
    mark_list.append(mark)
    mark = int(input('Enter ur marks : '))

print('the last input is', mark_list[-1])
print('the total number of input is', len(mark_list))
