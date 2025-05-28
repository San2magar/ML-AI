import math

'''
def area_of_circle(radius):
    return math.pi*radius**2

r=float(input('enter the radius of the circle'))

print(f'the area of the circle is :{area_of_circle(r):.2f}')
'''

"""Wap to calculate a compound interest and the simple interest and 
find the differences between the simple interest and compound interest and print"""

def simple_interest(p,t,r):
    return (p*t*r)/100

def compound_interest(p,t,r):
    return p*((1 + (r/100))**t - 1)

p=float(input('enter principle'))
t=float(input('enter time'))
r=float(input('enter rate'))

print(f'the simple interest :{simple_interest(p,t,r):.2f}')
print(f'the comp0und interest :{compound_interest(p,t,r):.2f}')



#wap a program using fibonacci series
