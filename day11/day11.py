data = []

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        data.append(line.rstrip())

class Monkey():
    def __init__(self, start, div, true, false, func):
        self.start = start
        self.items = []
        self.new = 0
        self.true = true
        self.false = false
        self.div = div
        self.func = func
        self.freq = 0

        for i in self.start:
            self.items.append(i)

    def test(self, i):
        self.freq += 1
        new = self.func(i)//3
        if new % self.div == 0:
            return(self.true, new)
        else:
            return(self.false, new)

    def add(self, item):
        self.items.append(item)

    def delete(self, item):
        self.items.remove(item)

    def show_items(self):
        return(self.items)

    def print_items(self):
        return (self.freq)


monkey_list_t = [Monkey([93, 54, 69, 66, 71], 7, 7, 1, lambda x: x * 3), Monkey([89, 51, 80, 66], 19, 5, 7, lambda x: x * 17),
               Monkey([90, 92, 63, 91, 96, 63, 64], 13, 4, 3, lambda x: x + 1), Monkey([65, 77], 3, 4, 6, lambda x: x + 2),
               Monkey([76,68,94], 2, 0, 6, lambda x: x * x), Monkey([86, 65, 66, 97, 73, 83], 11, 2, 3, lambda x: x + 8),
               Monkey([78], 17, 0, 1, lambda x: x + 6), Monkey([89,57,59,61,87,55,55,88], 5, 2, 5, lambda x: x + 7)]

monkey_list = [Monkey([79,98], 23, 2, 3, lambda x: x * 19), Monkey([54,65,75,74], 19, 2, 0, lambda x: x + 6),
                    Monkey([79,60,97], 13, 1, 3, lambda x: x * x), Monkey([74], 17, 0, 1, lambda x: x + 3)]


for _ in range(20):
    for monkey in monkey_list:
        items = tuple(monkey.show_items())
        for i in items:
            where, new = monkey.test(i)
            monkey.delete(i)
            monkey_list[where].add(new)

freq = []
for monkey in monkey_list:
    print(monkey.print_items())
    freq.append(monkey.print_items())

largest_integer = max(freq)
freq.remove(largest_integer)
second_largest_integer = max(freq)

print(largest_integer * second_largest_integer)
