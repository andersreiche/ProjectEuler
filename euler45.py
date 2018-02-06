#Project euler problem 45

def is_triangle(N):
    return int((N*(N+1))/2)

def is_pentagonal(N):
    return int((N*(3*N-1))/2)

def is_hexagonal(N):
    return int(N*(2*N-1))

assert(is_triangle(285) == is_pentagonal(165) and is_pentagonal(165) == is_hexagonal(143))

N = 1000
for t in range(283, 10000):
    for p in range(140, N):
        for h in range(140, N):
            if is_triangle(t) == is_pentagonal(p) and is_triangle(t) == is_hexagonal(h):
                print(is_triangle(t))
