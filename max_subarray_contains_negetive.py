
def max_subarray_sum_naive(arr):
    """
    Function to find the maximum subarray sum using a naive approach.
    :param arr: List of integers (can include negative numbers)
    :return: Maximum subarray sum
    """
    n = len(arr)
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    
    # Iterate through all possible starting points of the subarray
    for i in range(n):
        # Iterate through all possible ending points of the subarray
        for j in range(i, n):
            # Calculate the sum of the subarray
            current_sum = sum(arr[i:j+1])
            # Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum


# Example usage:
if __name__ == "__main__":
    # An array that includes negative numbers
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    result = max_subarray_sum_naive(arr)
    print("Maximum Subarray Sum (Naive):", result)