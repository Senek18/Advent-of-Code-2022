input1 = []

with open("input_f.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        input1.append(line.rstrip())

print(input1)

tree = {}

curr_dir = []
list_ele = False
tree_index = 0
for path in input1:
    line = path.strip().split(" ")

    if "$ cd" in path:
        if path[-1] == ".":
            curr_dir.pop()
        else:
            curr_dir.append(path)
        list_ele = False
    elif "$ ls" in path:
        pass
    else:
        if "dir" in path:
            pass
        else:
            if curr_dir[-1][-1]=="/":
                dirr = ""
                for i in curr_dir:
                    dirr += i[-1]
                tree.update({dirr+line[1]: line[0]})
            else:
                dirr = ""
                for i,k in enumerate(curr_dir):
                    if i > 1:
                        dirr += "/" + k[-1]
                    else:
                        dirr += k[-1]
                tree.update({dirr+"/"+line[1]: line[0]})

print(tree)

folders = {}

print(tree.keys())

for key in tree.keys():
    key_s = key.split("/")
    current_folder = ""
    for a in range(1, len(key_s) - 1):
        current_folder += ("/" + key_s[a])

    if current_folder == "":
        current_folder = "/"

    # if folder exists, nothing happens, size of folder is added later
    folders.update({current_folder: 0})

for file_key,file_value in tree.items():

    for folder_key,folder_value in folders.items():

        if file_key.startswith(folder_key):
            folders[folder_key]+=int(file_value)

print("folders",folders)

size=0

for key, value in folders.items():
    #print("item",value)
    if value<=100000:
        size+=value

print("size",size)