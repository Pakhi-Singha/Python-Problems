#fibonacci with recursion
n = int(input('Enter number'))
def fib(n):
    fib1=0
    fib2=1
    i=1
    while(i<=n):
        print(fib1)
        m=fib1
        fib1=fib2
        fib2=m+fib1
        i=i+1
fib(n)