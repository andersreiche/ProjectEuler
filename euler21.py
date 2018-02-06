#Project euler problem 21

def divisorsum(N):
    res = 0
    for i in range(1, N):
        if N%i == 0:
            res += i
    return res

def check_amicable(N):
    if divisorsum(divisorsum(N)) == N and divisorsum(N) != divisorsum(divisorsum(N)):
        return True
    return False

final = 0
for i in range(10000):
    if check_amicable(i):
        final += i

print(final)
