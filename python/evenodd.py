# WaP a function that takes two numbers start and end,
#  and prints how many even and odd numbers exist in the range (inclusive)

x = int(input('enter the first number : '))
y = int(input('enter the second number : '))

c=0
b=0

for i in range(x+1,y):
    if i % 2 == 0:
        b = b + 1
    else:
        c = c + 1

print(f'{b} is the evens')
print(f'{c} is the odds')    