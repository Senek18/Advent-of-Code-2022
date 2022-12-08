input = []


def ascii_num(letter: str):
    number = ord(letter)
    if number in range(97, 123):
        return number - 96
    elif number in range(65, 91):
        return number - 38
    else:
        return 0


with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        input.append(line.rstrip())

priorities = 0
k = 0
for i in range(int(len(input)/3)):
    elf1 = set(input[k+i])
    elf2 = set(input[k+i+1])
    elf3 = set(input[k+i+2])
    k += 2
    common1 = elf1.intersection(elf2, elf3)
    priorities += ascii_num(list(common1)[0])

print(priorities)