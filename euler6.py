#Project euler problem 6

def sum_squares(N):
    res = 0
    for i in range(N+1):
        res += i**2
    return res

def square_sums(N):
    res = 0
    for i in range(N+1):
        res += i
    return res**2


assert sum_squares(10) == 385
assert square_sums(10) == 3025

print(square_sums(100)-sum_squares(100))
