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
        self.i = 20
        self.signal = []

    def noop(self):
        self.cycle += 1
        self.check()

    def addx(self, V):
        self.cycle += 1
        self.check()
        self.cycle += 1
        self.check()
        self.X += V


    def check(self):
        self.i = 20
        while self.i < 240:
            if self.cycle == self.i:
                self.signal.append(self.cycle * self.X)
                print(self.signal)
            self.i += 40

    def show(self):
        print("X:", self.X, "cycle:", self.cycle)
        print('Sum:', sum(self.signal[:6]))

run = Tube()

for line in program:
    temp = line.split()
    if temp[0] == "noop":
        run.noop()
    else:
        run.addx(int(temp[1]))

run.show()