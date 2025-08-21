
'''
we find mid as blow
mid = low + (high-low)//2
because it won't cause overflow in case of large integer.
basically we just finding the distance between high and low using (high-low) and then dividing it by
2 and then adding low to it. to find mid point near low

'''

def binary_search(array, target):
    # Initialize the search boundaries
    low = 0
    high = len(array) - 1

    while low <= high:  # Continue searching while there is a valid range
        # Calculate the middle index
        mid = low + (high - low) // 2

        # Check if the middle element is the target
        if array[mid] == target:
            return mid  # Target found, return the index

        # If target is larger, look in the right half
        elif array[mid] < target:
            low = mid + 1

        # If target is smaller, look in the left half
        else:
            high = mid - 1

    # Return -1 if the target is not found
    return -1


if __name__ == "__main__":
    # Sorted array to search
    array = [1, 3, 5, 7, 9, 11, 13]
    target = 7

    result = binary_search(array, target)
