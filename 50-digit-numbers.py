#project euler 13
res = 0
with open("50-digit-numbers.txt", "r") as f:
    content = f.read()

for row in content.split('\n'):
    if row != "":
        res = res + int(row)

print(res)
