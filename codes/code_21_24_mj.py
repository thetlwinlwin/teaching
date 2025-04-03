# 11
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',]
Readings = []

total_day = 0
num_of_hr = 0
hourly_reading = []
AVG_TEMP = []

while total_day < 7:
    my_string = 'enter tempt of '+DAYS[total_day]+' at '+str(num_of_hr)+ ' : '
    tempt = float(input(my_string))

    if tempt < 50.0 and tempt > -20.0:
        hourly_reading.append(tempt)
        num_of_hr += 1

    if num_of_hr == 24:
        Readings.append(hourly_reading)

        total = 0
        for i in hourly_reading:
            total = total + i
        AVG_TEMP.append(round(total/24,1))

        hourly_reading = []
        num_of_hr = 0
        total_day += 1
    

total = 0
for i in AVG_TEMP:
    total += i

AVG_TEMP_OF_WEEK = total/7


