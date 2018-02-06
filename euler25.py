#Project euler problem 25

#Python Fibbonaci

def fib(N):
    a = 0
    b = 1
    for i in range(N):
        c = a + b
        a = b
        b = c
        #print(c) #Prints the Fibonacci series except the first digit
        if len(str(c)) == 1000:
            print(i)

fib(1000000)
