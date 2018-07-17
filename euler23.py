# Project euler problem 23
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time
import math
start = time.time()
res = 0

def divisorSum(n):
    sum = 0
    for i in range(1, math.ceil(n/2) + 1):
        if n%i == 0:
            sum += i
    return sum

def isAbundant(n):
    if divisorSum(n) > n:
        return True
    return False

non_ab_sum = [x for x in range(0, 28123)]
abundantNumbers = []
for i in range(12, 28123):
    if isAbundant(i):
        abundantNumbers.append(i)

for i in range(len(abundantNumbers)):
	for j in range(i,28123):
		if abundantNumbers[i]+abundantNumbers[j] < 28123:
			#negating the value of the abundant sum from the list
			non_ab_sum[abundantNumbers[i]+abundantNumbers[j]] = 0
		else:
			break

#print(f"List of abundant numbers from 1 - 28123: {abundantNumbers}")
#print(f"The list contains {len(abundantNumbers)} numbers")


elapsed = time.time() - start
print(f"result: {sum(non_ab_sum)} found in {elapsed} seconds.")