def two_sum(nums, target):
    # Dictionary to store indices of numbers and their value
    hash_map = {}

    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in the hash map
        if complement in hash_map:
            # If found, return the indices of current number and complement
            return [hash_map[complement], i]
        
        # Otherwise, store the index of the current number in the hash map
        hash_map[num] = i
    
    # If no solution, return an empty list (or raise an exception)
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]