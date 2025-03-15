std_name = ['thet lwin','bubu','taw win','vincent','mh','ryan','unknown','bubu',]
is_found = False
person_name = input('Enter name to search : ')

for counter in range(len(std_name)):
    if std_name[counter] == person_name:
        print('student is at : ',counter)
        is_found = True


if is_found == False:
    print('student not in the list')