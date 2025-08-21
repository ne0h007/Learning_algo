def findFirstAndLastOccurrence(nums, target):
    def binarySearch(nums, target, searchFirst):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid  # Target found, update result
                if searchFirst:
                    right = mid - 1  # Narrow search to find first occurrence
                else:
                    left = mid + 1  # Narrow search to find last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    # Perform binary search for both first and last occurrence
    first = binarySearch(nums, target, searchFirst=True)
    last = binarySearch(nums, target, searchFirst=False)
    
    return [first, last]


# # Example Usage
# nums = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# print(findFirstAndLastOccurrence(nums, target))  # Output: [1, 3]



'''
Problem Statement:
Find a target element in a rotated sorted array

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    

nums = [4,5,6,7,8,9,0,1,2]
target = 0

sl = Solution()
sl.search(nums, target)