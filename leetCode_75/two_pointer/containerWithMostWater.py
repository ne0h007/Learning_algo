'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water the container can contain is 49.
'''

def maxWater_naive(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
          
            # calculate the amount of water
            amount = min(arr[i], arr[j]) * (j - i)
          
            # keep track of maximum amount of water
            res = max(amount, res)
    return res

def maxWater(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:
        
        # find the water stored in the container between 
        # arr[left] and arr[right]
        water = min(arr[left], arr[right]) * (right - left)
        res = max(res, water)
        
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return res

  

if __name__ == "__main__":
	arr = [2, 1, 8, 6, 4, 6, 5, 5]
	print(maxWater(arr))