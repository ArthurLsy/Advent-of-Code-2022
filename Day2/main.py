#A Rock B Paper C Cisor
#X Rock Y Paper Z Cisor

file = open('input.txt', 'r')

input = file.readlines()

score = 0
score2 = 0

for i in range(len(input)):
    input[i] = input[i].replace('\n', '')
    input[i] = input[i].replace(' ', '')

def part1():
    global score
    for i in range(len(input)):
        if input[i][0] == 'A':
            if input[i][1] == 'X': #Nul
                score = score+4
            if input[i][1] == 'Y': #Win
                score = score+8
            if input[i][1] == 'Z': #Loose
                score = score+3
        if input[i][0] == 'B':
            if input[i][1] == 'X': #Loose
                score = score+1
            if input[i][1] == 'Y': #Nul
                score = score+5
            if input[i][1] == 'Z': #Win
                score = score+9
        if input[i][0] == 'C':
            if input[i][1] == 'X': #Win
                score = score+7
            if input[i][1] == 'Y': #Loose
                score = score+2
            if input[i][1] == 'Z': #Nul
                score = score+6

    return score

def part2():
    global score2
    for i in range(len(input)):
        if input[i][0] == 'A':
            if input[i][1] == 'X': #Loose
                score2 = score2+3
            if input[i][1] == 'Y': #Nul
                score2 = score2+3+1
            if input[i][1] == 'Z': #Win
                score2 = score2+6+2
        if input[i][0] == 'B':
            if input[i][1] == 'X': #Loose
                score2 = score2+1
            if input[i][1] == 'Y': #Nul
                score2 = score2+3+2
            if input[i][1] == 'Z': #Win
                score2 = score2+6+3
        if input[i][0] == 'C':
            if input[i][1] == 'X': #Loose
                score2 = score2+2
            if input[i][1] == 'Y': #Nul
                score2 = score2+3+3
            if input[i][1] == 'Z': #Win
                score2 = score2+6+1

    return score2






print('Partie 1 : ',part1())
print('Partie 2 : ',part2())

