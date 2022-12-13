import numpy as np

program = []

with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        program.append(line.rstrip())

print(program)


class Tube():
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.i = 0
        self.line = ""
        self.signal = []

    def noop(self):
        self.CRT()
        self.cycle += 1
        self.check()

    def addx(self, V):
        self.CRT()
        self.cycle += 1
        self.check()
        self.CRT()
        self.cycle += 1
        self.check()
        self.X += V

    def CRT(self):
        if self.cycle in [self.X-1, self.X, self.X+1]:
            self.line += "#"
        else:
            self.line += "."

    def check(self):
        if self.cycle == 40:
            self.signal.append(self.line)
            self.line = ""
            self.cycle = 0

    def show(self):
        file = open('output.txt', 'w')

        file.writelines("% s\n" % data for data in self.signal)
        file.close()
        print(self.signal)

run = Tube()

for line in program:
    temp = line.split()
    if temp[0] == "noop":
        run.noop()
    else:
        run.addx(int(temp[1]))

run.show()