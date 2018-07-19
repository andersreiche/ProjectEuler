#Project euler problem 24
# find the millionth lexiografic permutation of 0123456789
import itertools

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L = list(itertools.permutations(L)) #This function already uses lexiografic order, so no need to account for that explicitly (else they could be sorted)

print(L[999999])