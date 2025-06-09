
def fibo(n):
    fib_series=[]
    a,b =0,1

    for _ in range(n): #_ if range not defined
        fib_series.append(a)
        a, b = b , a+b
    return fib_series

n = int(input('enter a number'))

if n<0:
    print('the number cannot be negative')
else:
    print(f'the fibonacci series:{fibo(n)}')   
    