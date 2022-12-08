xyz = {"X": 1, "Y": 2, "Z": 3}
input = []

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()
        input.append(line.rstrip())

        if not line:
            break

count = 0
for i in input[:-1]:
    p1 = i[0]
    p2 = i[2]

    if p1 == "A":
        if p2 == "X":
            temp = xyz[p2] + 3
        elif p2 == "Y":
            temp = xyz[p2] + 6
        else:
            temp = xyz[p2]
    elif p1 == "B":
        if p2 == "X":
            temp = xyz[p2] + 0
        elif p2 == "Y":
            temp = xyz[p2] + 3
        else:
            temp = xyz[p2] + 6
    else :
        if p2 == "X":
            temp = xyz[p2] + 6
        elif p2 == "Y":
            temp = xyz[p2] + 0
        else:
            temp = xyz[p2] + 3

    count += temp

print(count)
