import math

def cylinder(r,h):
    return math.pi*r**2*h

def cone(r,l):
    return(math.pi*r**l)/3

r=float(input('enter radius'))
h=float(input('enter height'))
l=float(input('enter length'))

print(f'the cyinder :{cylinder(r,h):.2f}')
print(f'the cone :{cone(r,l):.2f}')
