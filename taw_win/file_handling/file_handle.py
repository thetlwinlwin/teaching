text = input('Say sth about Taw Win : ')

file = open('taw_win_bio.txt','w')
file.write(text)

file.close()