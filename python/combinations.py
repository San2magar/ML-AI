'''
 2. Compute combination ( C(n,k)) without using built-in functions
 Calculate the binomial coefficient:
 efficiency without using Python's built-in functions.
'''

def factorial(num):
    '''
    Compute factorial of a number num.
    factorial of num is the product of all positive integers up to num.
    for eg. 5! = 5 * 4 * 3 * 2 * 1 = 120
    '''
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def nCr(n,k):
    ''' 
    compute arithmetic C(n,k) = n! / ( k! * (n - k)!)
    which represents the number of the ways to choose k items from n items without repetition.
    '''

    if k > n:
        return 0 # combination not defined if k > n
    
    #calc factorial of n, k and (n-k)
    fact_n = factorial(n)
    fact_k = factorial(k)
    fact_n_k = factorial(n - k)

    # use the formula to compute the combination value
    combination = fact_n // (fact_k * fact_n_k)
    return combination

# Example usage:
# n,k =10,3

n = int(input("enter the value of n :"))
k = int(input("enter the value of k :"))
print(f'C({n}, {k})= {nCr(n,k)}')