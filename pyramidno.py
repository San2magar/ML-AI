
def star(n):
    a = 1
    for i in range(n):
        spaces = " " * (n-i-1)
        stars =  str(a) * (2*i+1)
        print(spaces + stars)
        a = a+1

if __name__ == '__main__':
    row = int(input("Enter the number of rows :"))
    print(star(row))