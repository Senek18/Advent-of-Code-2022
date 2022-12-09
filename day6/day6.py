input1 = []
with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        input1.append(line.rstrip())

end_arr = []
for i in input1:
    start = 0
    end = 14

    while True:
        chain = i[start:end]
        if len(set(chain)) == len(chain):
            break
        start += 1
        end += 1
    end_arr.append(end)
print(end_arr)