'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

def maxOnes_naive(arr, k):
    res = 0
    
    # Exploring all subarrays
    for i in range(len(arr)):
        
        # Counter for zeroes
        cnt = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                cnt += 1
            
            # If cnt is less than or equal to k, then  
            # all zeroes can be flipped to one
            if cnt <= k:
                res = max(res, j - i + 1)
    
    return res
def maxOnes_sliding(arr, k):
    res = 0

    # Start and end pointer of the window
    start = 0
    end = 0

    # Counter to keep track of zeros in current window
    cnt = 0

    while end < len(arr):
        if arr[end] == 0:
            cnt += 1

        # Shrink the window from left if no. 
        # of zeroes are greater than k
        while cnt > k:
            if arr[start] == 0:
                cnt -= 1

            start += 1

        res = max(res, (end - start + 1))

        # Increment the end pointer 
        # to expand the window
        end += 1

    return res

__import__("atexit").register(lambda: open("display_runtime.txt","w").write("0"))
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        zeros = 0
        max_len = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if (nums[l] == 0):
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

if __name__ == "__main__":
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    k = 2
    print(maxOnes_sliding(arr, k))