import ast

data = []
data_to_sort = []

with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        try:
            data.append(ast.literal_eval(line.rstrip()))
        except SyntaxError:
            data.append(line.rstrip())

data_len = len(data)
for i in range(0, data_len, 3):
    line_left = data[i]
    line_right = data[i+1]
    data_to_sort.append(line_left)
    data_to_sort.append(line_right)


def check_signal(left, right):
    left_type = type(left)
    right_type = type(right)
    if left_type == list and right_type == int:
        right = [right]
        right_type = type(right)

    if left_type == int and right_type == list:
        left = [left]
        left_type = type(left)

    if left_type == int and right_type == int:
        check = left < right
        if (left == right) is True:
            pass
        elif check is True:
            return 1
        elif check is False:
            return 0
    elif left_type == list and right_type == list:
        left_len = len(left)
        right_len = len(right)
        max_len = max(left_len, right_len)

        for j in range(max_len):
            try:
                left_line = left[j]
            except IndexError:
                return 1
            try:
                right_line = right[j]
            except IndexError:
                return 0
            stp = check_signal(left_line, right_line)
            if stp == 1:
                return 1
            elif stp == 0:
                return 0


def ins_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and (check_signal(key, arr[j]) == 0):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

ins_sort(data_to_sort)
data_to_sort.reverse()
idx_2 = data_to_sort.index([[2]])
print(idx_2)
idx_6 = data_to_sort.index([[6]])
print(idx_6)
print((idx_6+1)*(idx_2+1))





