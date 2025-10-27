file = open('lyrics.txt', 'w')

line = input('Write a line of lyric(type "end" to stop): ')

while line != 'end':
    file.write(line+'\n')
    line = input('Write a line of lyric(type "end" to stop): ')

file.close()
