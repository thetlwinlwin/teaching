quiz_list = [
    {
        "question": "To make the number sentence correct, what number should be added to 106 to equal 158",
        "answer": "52",
    },
    {
        "question": "What is the simplest form of 16/24",
        "answer": "2/3",
    },
    {
        "question": "Simon has 918 marbles. He wants to make packets of marbles, with nine marbles in each pack. How many packs will he be able to make",
        "answer": "102",
    },
    {
        "question": "If a rectangle has a length of 12 cm and a width of 5 cm, what is its perimeter",
        "answer": "34",
    },
    {
        "question": "Meena divides a number by 2 and then divides the result by 2 again. What is this equivalent to dividing the original number by",
        "answer": "4",
    },
    {
        "question": "Two angles of a triangle measure 35 degrees and 65 degrees. What is the measure of the third angle of the triangle",
        "answer": "80",
    },
]


marks = 0
for i in range(len(quiz_list)):
    print(f"\nNumber {i+1}")
    print(quiz_list[i]["question"])
    answer = input("\nEnter ur answer : ")
    if answer == quiz_list[i]["answer"]:
        marks += 1

print(f"Your final mark is {marks}")
