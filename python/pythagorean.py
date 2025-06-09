''' find all pythagorean triplets upto N
 wap to find all sets of integers (a, b, c) such that:

 [a^2 + b^2 = c^2 ] 
 and (a, b ,c <= N) .'''

def find_pythagorean_triplets(n):
    triplets=[]
    for c in range(1,n+1):
        for b in range(1,c):
            for a in range(1,b):
                if a * a + b *b == c*c:
                    triplets.append((a, b, c))

    return triplets

N = int(input("Enter the value of N : "))
triplets = find_pythagorean_triplets(N)
print(f'Pythagorean triplets up to {N}')     
for t in triplets:
    print(t)          