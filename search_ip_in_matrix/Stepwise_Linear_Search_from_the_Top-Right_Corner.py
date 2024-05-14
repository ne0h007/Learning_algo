'''
In this Python code, the search function begins searching from the top-right corner of the matrix. If the target is smaller than the current element, it moves left. If the target is larger, it moves down. The process repeats until the target is found, or the search area is exhausted. This method takes advantage of the row-wise and column-wise sorted property of the matrix to reduce the search space, producing more efficient results.

'''

def search(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    
    i = 0
    j = cols - 1
    
    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return f'Element {target} found at position ({i},{j})'
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
            
    return f'Element {target} not found'


# Test
matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
x = 37
print(search(matrix, x))  # Output: Element 37 found at position (2,2)

x = 100
print(search(matrix, x))  # Output: Element 100 not found