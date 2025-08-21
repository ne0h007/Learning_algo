# Function for finding first and last occurrence of x
def find(arr, x):
    n = len(arr)
    first = -1
    last  = -1

    for i in range(n):
        if arr[i] != x:
            continue
        if first == -1:
            first = i
        
        last = i
    return first, last

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125,]
    x = 5
    res = find(arr, x)
    print(res[0], res[1])


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

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                

# # Example Usage
# nums = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# print(findFirstAndLastOccurrence(nums, target))  # Output: [1, 3]