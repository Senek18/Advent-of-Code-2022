import numpy as np
data = []

with open("input", 'r') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        temp = []

        for i in line:
            temp.append(int(i))
        data.append(temp)
y_limit = len(data)
x_limit = len(data[1])
zeros = np.zeros((y_limit, x_limit))

count = (y_limit - 2) * 2 + (x_limit-2) * 2 + 4
ct = 0
cd = 0
cl = 0
cr = 0
for x in range(1, x_limit-1):
    for y in range(1, y_limit-1):
        tree = data[x][y]

        i = x - 1
        while i > -1:
            check = tree > data[i][y]
            if check is False:
                break
            ct += 1
            i -= 1

        if i == -1:
            zeros[x][y] = 1

        i = x + 1
        while i < x_limit:
            check = tree > data[i][y]
            if check is False:
                break
            cd += 1
            i += 1


        if i == x_limit:
            zeros[x][y] = 1

        i = y - 1
        while i > -1:
            check = tree > data[x][i]
            if check is False:
                break
            cl += 1
            i -= 1

        if i == -1:
            zeros[x][y] = 1

        i = y + 1
        while i < y_limit:
            check = tree > data[x][i]
            if check is False:
                break
            cr += 1
            i += 1

        if i == y_limit:
            zeros[x][y] = 1

print(zeros)
print(count + sum(sum(zeros)))


