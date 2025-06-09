def reverse(n):
    
    reverse_n = 0

    while n>0:
       digit= n%10
       reverse_n = reverse_n * 10 + digit
       n = n//10

    return reverse_n

n = int(input('enter a number'))

print(f'the reverse :{reverse(n)}') 