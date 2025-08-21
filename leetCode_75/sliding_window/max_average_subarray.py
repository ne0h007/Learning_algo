'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


'''
from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    res = sum(nums[:k])
    for i in range(n-k+1):
        res = max(res , sum(nums[i:i+k]))
    return res/4

# driver code

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(findMaxAverage(nums,k))