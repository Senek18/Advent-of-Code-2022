input1 = []
with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        input1.append(line.rstrip())

# creat stacks list
n = 0
k = 1
# check number of stacks
for k, line in enumerate(input1):
    if line.strip(" ")[0] == "1":
        n = int(input1[k][-1])
        break
# creat n number of stack
stacks = [[] for i in range(n)]

for i in range(k-1, -1, -1):
    for num, stack in enumerate(stacks):
        try:
            temp = input1[i][1 + num * 4]
            if temp == " ":
                continue
            stack.append(temp)
        except IndexError:
            continue

for i in input1[n + 1:]:
    line = i.split(" ")
    var = []
    for k in line:
        try:
            temp = int(k)
            var.append(temp)
        except ValueError:
            continue
    temp = []
    for j in range(var[0]):
        temp.append(stacks[var[1]-1].pop())
    temp.reverse()
    for k in temp:
        stacks[var[2]-1].append(k)

output = ""
for i in stacks:
    try:
        output += i[-1]
    except IndexError:
        output += " "
print(output)