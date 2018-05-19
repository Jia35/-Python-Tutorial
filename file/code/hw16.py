def Fibonacci(n):
    result = 0
    if n==0:
        result = 0
    elif n==1:
        result = 1
    else:
        result = Fibonacci(n-1)+Fibonacci(n-2)
    return result

for i in range(10):
    print(Fibonacci(i))
