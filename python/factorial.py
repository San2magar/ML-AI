def fac(n):
    return int(str(abs(num))[::-1])

a=int(input('enter a number for factorial'))

def fact(a):
    s=1
    if a==0:
        return 1
    else:
        while a>0:
            s=s*a
            a=a-1
        return s
print(fact(a))