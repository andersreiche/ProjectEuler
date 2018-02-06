#Project Euler Problem 5
def is_divisible (N):
    if N%1 == 0 and N%2 == 0 and N%3 == 0 and N%4 == 0 and N%5 == 0 and N%6 == 0 and N%7 == 0 and N%8 == 0 and N%9 == 0:
        if N%10 == 0 and N%11 == 0 and N%12 == 0 and N%13 == 0 and N%14 == 0 and N%15 == 0 and N%16 == 0 and N%17 == 0 and N%18 == 0:
            if N%19 == 0 and N%20 == 0:
                return 1
    return 0

for i in range(1,1000000000):
    if is_divisible(i):
        print(i)
