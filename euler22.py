#Project euler problem 22

def namescore(name = []):
    res = 0
    for i in range(len(name[0])):
        if ord(name[0][i]) >= ord('A') and ord(name[0][i]) <= ord('Z'):
            res += (ord(name[0][i]) -64)
    return res

with open("names.txt", "r") as f:
    content = f.read()

names = list()
for name in content.split(','):
    if name != "":
        L = name.split()
        names.append(L)


names = sorted(names)
res = 0
index = 1
for name in names:
    res += (namescore(name) * index)
    index += 1

print(res)



