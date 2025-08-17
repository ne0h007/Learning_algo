'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 
 '''



def pushZerosToEnd_1(arr=None):
    tmp = [0]*len(arr)
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            tmp[j] = arr[i]
            j += 1
    
    for i in range(len(arr)):
        arr[i] =  tmp[i]


def pushZerosToEnd_2(arr):
    # will take two traversal
    # Count of non-zero elements
    count = 0  

    # If the element is non-zero, replace the element at
    # index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
        count += 1

def pushZerosToEnd(arr):
    # in one traversal only
    # Pointer to track the position
    # for next non-zero element
    count = 0
    
    for i in range(len(arr)):
        
        # If the current element is non-zero
        if arr[i] != 0:
            
            # Swap the current element with
            # the 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            
            # Move 'count' pointer to the next position
            count += 1



if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")



