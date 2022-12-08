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

def part2():
    global letters

    letter = letters
    total = 0
    lines = []

    with open("input.txt") as file:
        counter = 0
        start = 0
        stop = 3
        for line in file:
            lines.append(line.strip())
            curr_group = lines[start:stop]
            counter += 1

            if counter % 3 == 0:
                for letter in curr_group[0]:
                    if letter in curr_group[1]:
                        if letter in curr_group[2]:
                            total += letters.index(letter) + 1
                            break
                start += 3
                stop += 3

    return total


print('Partie 1 :', part1())

print('Partie 2 :', part2())