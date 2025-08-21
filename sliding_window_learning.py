'''
for fixed size windows 
'''

def max_subarray_sum_k(arr, k):
    max_sum = 0
    window_sum = 0
    start = 0
    
    # Loop through the array
    for end in range(len(arr)):
        # Add the next element to the window
        window_sum += arr[end]

        # Check if window size is reached
        if end - start + 1 == k:
            # Update maximum sum
            max_sum = max(max_sum, window_sum)

            # Slide the window forward and remove the first element
            window_sum -= arr[start]
            start += 1

    return max_sum

def longest_substring_k_distinct(s, k):
    char_count = {}
    start = 0
    max_length = 0

    # Loop through the string
    for end in range(len(s)):
        # Add the character at the `end` position to the dictionary
        right_char = s[end]
        if right_char not in char_count:
            char_count[right_char] = 0
        char_count[right_char] += 1

        # Shrink the window until there are `k` distinct characters in the window
        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1

        # Update the maximum length
        max_length = max(max_length, end - start + 1)

    return max_length

# Test the function
s = "araaciaaaaaaaaaraaaaaaaa"
k = 2
print(longest_substring_k_distinct(s, k))  # Output: 4 (The substring "araa" has the longest length)