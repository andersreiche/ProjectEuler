#Project euler problem 18

with open("Maximum_path_sum_1.txt", "r") as f:
    content = f.read()

res = 0
for row in content.split('\n'):
    if row != "":
        L = row.split()
        res += 