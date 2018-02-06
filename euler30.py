#Project euler problem 30
res = 0
for i in range(2, 1000000):
    temp = 0
    i_string = str(i)
    L = list(i_string)
    for j in range (0, len(L)):
        integer = int(L[j])
        temp += integer**5
    if temp == i:
        res += temp
print(res)
