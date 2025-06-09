import math

def rev_factorial(n):

    return int(str(abs(n))[::-1]) # reverse string
    
    
n = int(input('enter a number'))

n= math.factorial(n)

print(rev_factorial(n))
