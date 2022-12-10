import numpy as np
data = []

with open("input_f.txt", 'r') as file:
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

for x in range(1, x_limit-1):
    for y in range(1, y_limit-1):
        tree = data[x][y]

        i = x - 1
        ct = 0
        while i > -1:
            check = tree > data[i][y]
            ct += 1
            if check is False:
                break
            i -= 1

        i = x + 1
        cd = 0
        while i < x_limit:
            check = tree > data[i][y]
            cd += 1
            if check is False:
                break
            i += 1

        i = y - 1
        cl = 0
        while i > -1:
            check = tree > data[x][i]
            cl += 1
            if check is False:
                break
            i -= 1

        i = y + 1
        cr = 0
        while i < y_limit:
            check = tree > data[x][i]
            cr += 1
            if check is False:
                break
            i += 1

        zeros[x][y] = ct * cd * cl * cr

print(np.max(zeros))
