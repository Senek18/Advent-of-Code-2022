import numpy as np
import sys
from dijsktra_algo import Graph

data = []
start, end = None, None
count = 0

with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        data.append(line.rstrip())
map = np.zeros((len(data), len(data[1])))

for idx, line in enumerate(data):
    for jdx, j in enumerate(line):
        if j == "S":
            start = [idx, jdx]
            map[idx][jdx] = ord("a")
        elif j == "E":
            end = [idx, jdx]
            map[idx][jdx] = ord("z")
        else:
            if j == "a":
                count += 1
            map[idx][jdx] = ord(j)
print("Liczba a: ",count)

print(map, start, end)
y = len(map)
x = len(map[0])
graph = []
for idx, i in enumerate(map):
    for jdx, j in enumerate(i):
        temp_list = np.zeros(x*y)
        pos = idx * x + jdx
        if jdx > 0:
            check = map[idx, jdx-1] - map[idx, jdx]
            if check <= 1:
                temp_list[pos - 1] = 1
            else:
                temp_list[pos - 1] = 0

        try:
            check = map[idx, jdx + 1] - map[idx, jdx]
            if check <= 1:
                temp_list[pos + 1] = 1
            else:
                temp_list[pos + 1] = 0
        except IndexError:
            pass

        if idx > 0:
            check = map[idx-1, jdx] - map[idx, jdx]
            if check <= 1:
                temp_list[pos - x] = 1
            else:
                temp_list[pos - x] = 0

        try:
            check = map[idx+1, jdx] - map[idx, jdx]
            if check <= 1:
                temp_list[pos + x] = 1
            else:
                temp_list[pos + x] = 0
        except IndexError:
            pass

        graph.append(list(temp_list.astype(int)))

g = Graph(x*y)
g.graph = graph
g.dijkstra(start[0]*x+start[1],end[0]*x+end[1])

