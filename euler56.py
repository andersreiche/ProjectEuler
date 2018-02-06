#Project euler problem 56
import time
start = time.time()

largest = 0
def digitsum(val):
    res = 0
    stringval = str(val)
    L = list(stringval)

    for i in range(len(L)):
        res += int(L[i])
    return res

for a in range(1,100):
    for b in range(1,100):
        temp = digitsum(a**b)
        if temp > largest:
            largest = temp




print(largest)
elapsed = (time.time() - start)
print(f"time elapsed: {elapsed} seconds")