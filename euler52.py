#Project euler problem 52
import time
start = time.time()

def stringify(N):
    stringN = str(N)
    stringN = list(stringN)
    stringN = sorted(stringN)
    return stringN

def permutable(N):
    if stringify(N) == stringify(2 * N):
        if stringify(N) == stringify(3 * N):
            if stringify(N) == stringify(4 * N):
                if stringify(N) == stringify(5 * N):
                    if stringify(N) == stringify(6 * N):
                        return 1
    return 0

for n in range(1, 1000000):
    if permutable(n):
        print(n)
        break

elapsed = (time.time() - start)
print(f"time elapsed: {elapsed} seconds")
