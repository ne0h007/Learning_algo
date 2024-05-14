'''
However, this method is not applicable to regular row-wise and column-wise sorted matrices. Also, it includes the function map_to_mat_index that maps a 1D index back to 2D indices in the original matrix. But this method fails when elements between rows don't hold a sorted relationship.
'''

def map_to_mat_index(idx, mat):
    n_col = len(mat[0])
    row_idx = idx // n_col
    col_idx = idx % n_col
    return (row_idx, col_idx)

def search(mat, target):
    n_row = len(mat)
    n_col = len(mat[0])
  
    left = 0
    right = n_row * n_col - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = mat[map_to_mat_index(mid, mat)[0]][map_to_mat_index(mid, mat)[1]]
    
        if mid_element == target:
            return "Element found at " + str(map_to_mat_index(mid, mat))
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return "Element not found"

mat = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
# mat = [
# [1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]
# ]

print(search(mat,11))

'''
The third method, "Treat the Matrix as a Sorted One-Dimensional Array O(log(mn))", can fail when the given matrix is sorted row-wise and column-wise, but not globally sorted.

In a globally sorted matrix, the elements in the second row are greater than all the elements in the first row, the elements in the third row are greater than all the elements in the second row, and so on. Also, elements in later columns are greater than all elements in earlier columns.

However, in a row-wise and column-wise sorted matrix, the elements are sorted in each row and in each column separately, but there's no guarantee that all elements in later rows/columns are larger than all elements in earlier rows/columns.

For instance, if we have a matrix like this:

1 2 3
4 5 6
7 8 9

The matrix is globally sorted and we can apply the third method. But if our matrix looks like this:

1 4 7
2 5 8
3 6 9

This matrix is sorted row-wise and column-wise, but it is not globally sorted. For instance, number '2' is in the second row while the first row contains numbers larger than '2'.

In a globally sorted matrix, all elements of row 'i' are less than all elements of row 'i+1' ∀ i, and similarly for columns.

This matrix is sorted row-wise and column-wise, but is not globally sorted because the elements in later rows are not greater than all elements in earlier rows.

This method would fail to correctly find the position of an element in the second matrix because when it converts this 2D matrix to a 1D matrix and applies binary search, it considers the entire matrix as a globally sorted array, which isn't actually the case.

'''