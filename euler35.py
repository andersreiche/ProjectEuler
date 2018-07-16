#Project euler problem 35

# How many circular primes are there below one million?
from math import sqrt
from itertools import count, islice

import time
start = time.time()

def rotate(l, n):
    return l[n:] + l[:n]

def isPrime(n):
    if n < 2:
        return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False
    return True

def isCircularPrime(n):
    if isPrime(n):
        numString = str(n)
        l = list(numString)
        for permutation in range (1, len(numString)):
            x = ''.join((rotate(l,permutation)))
            x = int(x)
            if isPrime(x) == False:
                return False
    else:
        return False
    return True

res = 0
for i in range (1,1000001):
    if isCircularPrime(i):
        res += 1

elapsed = time.time() - start
print(res)
print(f"result: {res} found in {elapsed} seconds.")