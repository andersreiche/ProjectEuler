#Project euler problem 55
import time
start = time.time()

def is_palindrome(val):
    stringval = str(val)
    if stringval == stringval[::-1]:
        return 1
    else:
        return 0

def reverse(val):
    return int(str(val)[::-1])

res = 0
num = 0
for i in range(1,10000):
    iteration = 0
    num = i + reverse(i)
    while iteration < 50:
        if is_palindrome(num) == 1:
            break
        num = num + reverse(num)
        iteration += 1
        if iteration == 50:
            res += 1


print(res)
elapsed = (time.time() - start)
print(f"time elapsed: {elapsed} seconds")