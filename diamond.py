
def star(n):
    for i in range(n):
        spaces = " " * (n-i-1)
        stars = "*" * (2*i+1)
        print(spaces + stars)

    for i in range(n-2,-1,-1):
        spaces = " " * (n-i-1)
        stars = "*" * (2*i+1)
        print(spaces + stars)

if __name__ == '__main__':
    row = int(input("Enter the number of rows :"))
    print(star(row))