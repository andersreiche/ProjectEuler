#Project euler problem 20

def factorial(n):
    return 1 if (n < 1) else n * factorial(n-1)

number_string = str(factorial(100))
L = list(number_string)

res = 0
for i in range(0, len(L)):
    res += int(L[i])

print(res)
