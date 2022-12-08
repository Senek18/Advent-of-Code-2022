input = []
count = 0
with open("input.txt", 'r') as file:
    while True:
        count += 1
        line = file.readline()
        input.append(line.rstrip())

        if not line:
            break
cal = []
temp = 0
for i in input:
    if i == "":
        cal.append(temp)
        temp = 0
    else:
        temp = temp + float(i)
print(max(cal))

highest_three = sorted(cal, reverse=True)[:3]
print(sum(highest_three))
