# Array # list
# Data Structure
# [element0,element1,element2] 

# it can store any data type

string_array = ['Vincent', 'Hi','Tech']
int_array = [1,2,3100]
float_array = [2.5,0.06]

# It can mix the data type
vincent_array = [
    "Vincent",
    70,
    153.6
]

# It can only another array
array_list = [
    'Bam',
    27.86,
    ['Vincent','Pro',12]
]


# can add element
# at any index
string_array.append("Noob")
# => ['Vincent', 'Hi', 'Tech', 'Noob']

string_array.insert(0,'vin')
# => ['vin', 'Vincent', 'Hi', 'Tech', 'Noob']


# can change the element
string_array[3] = 'Art'
# => ['vin', 'Vincent', 'Hi', 'Art', 'Noob']

# can delete the element
del string_array[0]
# => ['Vincent', 'Hi', 'Art', 'Noob']

string_array.pop(1)
# => ['Vincent', 'Art', 'Noob']

another_array = ['a','b','b','c']
another_array.remove('b')
# => ['a','b','c']

# remove the last element
another_array.pop()
# => ['a','b']

# remove all the element
another_array.clear()
# => []



marking_table = [
    ['Vincent',100,'Hello Kitty'],
    ['Thet Lwin',101,'All subs'],
    ['Skibidi',2, 'Toilet']
]

           # 0   1   2   3
my_array = ['A','b', 1, 5]
           # -4 -3  -2  -1 

