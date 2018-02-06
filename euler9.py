#Project euler problem 9
N = 1000

for a in range(N):
    for b in range(N):
        for c in range(N):
            if a < b and b < c and a+b+c == 1000 and a**2 + b**2 == c**2:
                print(a*b*c)
