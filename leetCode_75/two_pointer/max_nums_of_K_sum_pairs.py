'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

'''


def maxPairs(nums, k):
    '''
    Time Complexity = O(nlogn)
    space = O(1)
    '''
    nums = sorted(nums)

    result = 0

    start, end = 0, len(nums) - 1
    
    while (start < end):
        if (nums[start] + nums[end] > k):

            end -= 1

        elif (nums[start] + nums[end] < k):

            start += 1
            
        else:
            start += 1
            end -= 1
            result += 1

    print(result)


def maxPairs_using_dict(nums, k) :
    
    m = {}    
    result = 0

    for i in nums :        
        if ((i in m) and m[i] > 0) :        
            m[i] = m[i] - 1
            result += 1
        else :        
            if k - i in m :
                m[k - i] += 1
            else :
                m[k - i] = 1
    
    print(result)

# Driver Code
if __name__ == '__main__':
    
    arr = [ 1, 2, 3, 4 ]
    K = 5

    maxPairs(arr, K)
    
