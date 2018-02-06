#Project Euler Problem 4
x = 0
def is_palindrome(val):
    stringval = str(val)
    if stringval == stringval[::-1]:
        return 1
    else:
        return 0

for i in range(1,1001):
    for j in range(1,1001):
        if is_palindrome(i*j):
            y = i*j
            if y > x:
                x = y
print(x)
