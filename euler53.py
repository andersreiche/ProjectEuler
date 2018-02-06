#Project euler problem 53
import time
start = time.time()

def factorial(n):
    return 1 if (n < 1) else n * factorial(n-1)

def ncr(n, r):
    return ( factorial(n) ) / ( factorial(r) * factorial(n-r))

res = 0
for n in range(23,101):
    for r in range(1,101):
        if r > n: break
        if ncr(n,r) > 1000000:
            res += 1
print(res)
elapsed = (time.time() - start)
print(f"time elapsed: {elapsed} seconds")