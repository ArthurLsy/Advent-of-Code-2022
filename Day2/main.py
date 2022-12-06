#A Rock B Paper C Cisor
#X Rock Y Paper Z Cisor

file = open('input.txt','r')

input = file.readlines()

score = 0

for i in range(len(input)):
    input[i] = input[i].replace('\n','')
    input[i] = input[i].replace(' ','')

for i in range(len(input)):
    if input[i][0] == 'A':
        if input[i][1] == 'X':
            score = score+2
        if input[i][1] == 'Y':
            score = score+8
        if input[i][1] == 'Z':
            score = score+3
    if input[i][0] == 'B':
        if input[i][1] == 'X':
            score = score+1
        if input[i][1] == 'Y':
            score = score+4
        if input[i][1] == 'Z':
            score = score+9
    if input[i][0] == 'C':
        if input[i][1] == 'X':
            score = score+7
        if input[i][1] == 'Y':
            score = score+2
        if input[i][1] == 'Z':
            score = score+6

print(score)