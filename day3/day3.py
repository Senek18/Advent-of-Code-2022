input = []


def ascii_num(letter: str):
    number = ord(letter)
    if number in range(97, 123):
        return number - 96
    elif number in range(65, 91):
        return number - 38
    else:
        return 0


with open("input.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        input.append(line.rstrip())

priorities = 0
for i in input:
    half = int(len(i)/2)
    first_comp = set(i[:half])
    second_comp = set(i[half:])
    common = first_comp.intersection(second_comp)
    priorities += ascii_num(list(common)[0])

print(priorities)