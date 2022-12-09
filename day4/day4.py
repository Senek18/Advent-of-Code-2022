count1 = 0
count2 = 0
with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        temp = line.rstrip()

        elf = []
        for j in temp.split(","):
            left, right = j.split("-")
            elf.append(int(left))
            elf.append(int(right))

        e1 = set([i for i in range(elf[0], elf[1]+1)])
        e2 = set([i for i in range(elf[2], elf[3]+1)])

        if e1.issubset(e2) is True or e2.issubset(e1) is True:
            count1 += 1
        if e1.isdisjoint(e2) is False:
            count2 += 1

print(count1, count2)


