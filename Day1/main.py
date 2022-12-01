input = open('input.txt', 'r')

tab_valeur = input.readlines()

tab_elf = [[]]

tab_elf_final = []

incr = 0

elf_before = 0

result = 0


for i in range(len(tab_valeur)):
    if tab_valeur[i] == '\n':
        incr = incr + 1
        tab_elf.append([])
    if tab_valeur[i] != '\n':
        tab_elf[incr].append(int(tab_valeur[i].replace('\n','')))

for i in range(len(tab_elf)):
    temp_value = 0
    for j in range(len(tab_elf[i])):
        temp_value = temp_value + tab_elf[i][j]
    tab_elf_final.append(temp_value)


print('Partie 1 : ', max(tab_elf_final))

top3 = 0

for i in range(3):
    top3 = top3 + max(tab_elf_final)
    tab_elf_final[tab_elf_final.index(max(tab_elf_final))] = 0

print('Partie 2 : ', top3)
