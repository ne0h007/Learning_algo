'''
Given a matrix where each row and each column is sorted in ascending order, identify the most efficient method for searching a specific element in terms of time complexity


In this Python code, the binary_search function takes a list arr and a number x and conducts a binary search for x in arr. The search function iterates through each row in the 2d list mat, and runs binary_search on it. If the element is found, it returns a string with its position. If it's not found in any row, it returns a 'not found' message.

'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # x is present at the mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
def search(mat, target):
    for i in range(len(mat)):
        j = binary_search(mat[i], target)
        if j != -1:
            return f'Element {target} found at position ({i},{j})'
    return f'Element {target} not found'


# Test
mat = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
x = 37
print(search(mat, x))         # Output: Element 37 found at position (2,2)

x = 100
print(search(mat, x))         # Output: Element 100 not found