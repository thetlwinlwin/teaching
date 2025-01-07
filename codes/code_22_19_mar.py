TOTAL_STUDENTS = 60
AVAILABLE_SUBS = ["phy", "chem", "his", "geo", "cs"]
student_name = []
first_choice = []
second_choice = []

# Task 1

# 0 should be TOTAL_STUDENTS
for _ in range(0):
    name = input("Enter the name : ")
    sub_1 = int(input("Enter sub phy(1),chem(2),his(3),geo(4),cs(5) : "))
    sub_2 = int(input("Enter sub phy(1),chem(2),his(3),geo(4),cs(5) : "))
    student_name.append(name)
    first_choice.append(sub_1)
    second_choice.append(sub_2)

with open("taw_win/data.csv") as file:
    for line in file:
        line = line.removesuffix("\n")
        data = line.split(",")
        student_name.append(data[0])
        first_choice.append(int(data[1]))
        second_choice.append(int(data[2]))

for i in range(len(AVAILABLE_SUBS)):
    sub_name = AVAILABLE_SUBS[i]
    total = 0
    for ii in first_choice:
        if ii == i + 1:
            total += 1
    for iii in second_choice:
        if iii == i + 1:
            total += 1

    print(f"For {sub_name}, total student is {total}")


# Task 2

phy = []
chem = []
his = []
geo = []
cs = []

total_in_each = [0, 0, 0, 0, 0]

one_sub_reject = []
two_sub_reject = []

for i in range(len(student_name)):
    sub_1 = first_choice[i]
    sub_2 = second_choice[i]
    name = student_name[i]
    is_sub_1_rejected = False
    is_sub_2_rejected = False

    if sub_1 == 1 and len(phy) < 40:
        phy.append(name)
        total_in_each[0] += 1
    if sub_1 == 2 and len(chem) < 40:
        chem.append(name)
        total_in_each[1] += 1
    if sub_1 == 3 and len(his) < 40:
        his.append(name)
        total_in_each[2] += 1
    if sub_1 == 4 and len(geo) < 40:
        geo.append(name)
        total_in_each[3] += 1
    if sub_1 == 5 and len(cs) < 40:
        cs.append(name)
        total_in_each[4] += 1
    else:
        is_sub_1_rejected = True

    if sub_2 == 1 and len(phy) < 40:
        phy.append(name)
        total_in_each[0] += 1
    if sub_2 == 2 and len(chem) < 40:
        chem.append(name)
        total_in_each[1] += 1
    if sub_2 == 3 and len(his) < 40:
        his.append(name)
        total_in_each[2] += 1
    if sub_2 == 4 and len(geo) < 40:
        geo.append(name)
        total_in_each[3] += 1
    if sub_2 == 5 and len(cs) < 40:
        cs.append(name)
        total_in_each[4] += 1
    else:
        is_sub_2_rejected = True

    if is_sub_1_rejected and is_sub_2_rejected:
        two_sub_reject.append([name, sub_1, sub_2])
    else:
        if is_sub_1_rejected:
            one_sub_reject.append([name, sub_1])
        else:
            one_sub_reject.append([name, sub_2])

for i in one_sub_reject:
    print(f"{i[0]} got rejected to attend {i[1]}")

for i in two_sub_reject:
    print(f"{i[0]} got rejected to attend {i[1]} and {i[2]}")

total_spares = 0
for i in range(len(total_in_each)):
    each = total_in_each[i]
    if each < 20:
        print(f"{AVAILABLE_SUBS[i]} class has {20-each} spare places.")
        total_spares += 1

print(f"total unallocated is {len(one_sub_reject) + (len(two_sub_reject)*2)}")
print(f"total spare places is {total_spares}")
