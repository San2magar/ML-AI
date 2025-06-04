# Wap that takes a list of numbers and prints only the alternate elements, starting from index 0.

def alternateElements(num):
    for i in range(0, len(num), 2):
        print(num[i], end=" ")


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Alternate elements:", end=" ")
alternateElements(num_list)
