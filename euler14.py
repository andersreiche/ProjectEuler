#Project euler problem 14
x = 0
y = 0
def seq_len(N):
    length = 1
    while N != 1:
        if N%2 == 0:
            N = N/2
        else:
            N = (3*N)+1
        length += 1
    return length


for i in range(1,1000001):
    if x < seq_len(i):
        x = seq_len(i)
        y = i
print (y)
