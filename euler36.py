#Project euler problem 36

def is_palindrome(val):
    stringval = str(val)
    if stringval == stringval[::-1]:
        return 1
    else:
        return 0

def is_palindrome_bin(val):
    stringval = str(format(val, 'b'))
    if stringval == stringval[::-1]:
        return 1
    else:
        return 0

res = 0
for i in range(1,999999):
    if is_palindrome(i):
        if is_palindrome_bin(i):
            res += i

print(res)
