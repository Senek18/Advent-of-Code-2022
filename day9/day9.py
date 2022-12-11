import numpy as np

moves = []

with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        moves.append(line.rstrip())

print(moves)


class Move:
    def __init__(self):
        self.x_H = 500
        self.y_H = 500
        self.x_T = 500
        self.y_T = 500
        self.touch = True
        self.line = True
        self.map = np.zeros((self.x_H * 2 ,self.y_H * 2))

    def right(self):
        self.x_H += 1
        self.check()
        self.check_line()

        if self.touch is False:
            if self.line is True:
                self.x_T += 1
            else:
                self.y_T = self.y_H
                self.x_T += 1
        self.map[self.x_T, self.y_T] = 1


    def left(self):
        self.x_H -= 1
        self.check()
        self.check_line()

        if self.touch is False:
            if self.line is True:
                self.x_T -= 1
            else:
                self.y_T = self.y_H
                self.x_T -= 1
        self.map[self.x_T, self.y_T] = 1

    def up(self):
        self.y_H += 1
        self.check()
        self.check_line()

        if self.touch is False:
            if self.line is True:
                self.y_T += 1
            else:
                self.x_T = self.x_H
                self.y_T += 1
        self.map[self.x_T, self.y_T] = 1

    def down(self):
        self.y_H -= 1
        self.check()
        self.check_line()

        if self.touch is False:
            if self.line is True:
                self.y_T -= 1
            else:
                self.x_T = self.x_H
                self.y_T -= 1
        self.map[self.x_T, self.y_T] = 1

    def check(self):

        x_diff = abs(self.x_H - self.x_T)**2
        y_diff = abs(self.y_H - self.y_T)**2
        d = np.sqrt(x_diff + y_diff)
        if d == 1 or d == 0 or d == np.sqrt(2):
            self.touch = True
        else:
            self.touch = False

    def check_line(self):
        if self.x_H == self.x_T or self.y_H == self.y_T:
            self.line = True
        else:
            self.line = False

    def show(self):
        print("Head: ", [self.x_H, self.y_H])
        print("Tail:", [self.x_T, self.y_T])
        print(self.map)
        print(np.sum(self.map))


start = Move()

for i in moves:
    temp = i.split()
    if temp[0] == "R":
        for k in range(int(temp[1])):
            start.right()
    elif temp[0] == "L":
        for k in range(int(temp[1])):
            start.left()
    elif temp[0] == "U":
        for k in range(int(temp[1])):
            start.up()
    elif temp[0] == "D":
        for k in range(int(temp[1])):
            start.down()
start.show()
