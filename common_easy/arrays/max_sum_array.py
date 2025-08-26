def max_subarray(nums):
    # Initialize variables to track the current and maximum sums
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        # Update max_current to either the current number or the sum of the current number with max_current
        max_current = max(nums[i], max_current + nums[i])
        
        # Update max_global to track the maximum sum found so far
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print(result)  # Output: 6 (subarray: [4, -1, 2, 1])