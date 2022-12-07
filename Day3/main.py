import string

letters = list(string.ascii_lowercase + string.ascii_uppercase)

file = open('input.txt', 'r')

input = file.readlines()

for i in range(len(input)):
    input[i] = input[i].replace('\n', '')


def part1():
    global letters, input

    type = []

    score = 0

    def egal(temp1, temp2):
        for j in range(len(temp1)):
            for k in range(len(temp2)):
                if temp1[j] == temp2[k]:
                    return temp1[j]

    for i in range(len(input)):
        mid = int(len(input[i]) / 2)
        temp1 = input[i][0:mid]
        temp2 = input[i][mid:len(input[i])]
        type.append(egal(temp1, temp2))

    for i in range(len(type)):
        score = score + letters.index(type[i]) + 1

    return score





print('Partie 1 :', part1())
