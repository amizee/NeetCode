class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        
        return maxSum

# Intuition: Kadane's algorithm - general idea is if the current subarray is positive, continue with it otherwise reset the subarray. 
# The order you do things is very important here, if you only have negative numbers or zeroes you still have to take the max of the currentMax and the negative number.
# For each index, you ALWAYS add the number to currSum after and compare it with the global max, and only reset it on the next iteration if the sum < 0
# Similar to how in Daily Temperatures you always add the current temperature to the stack, and handle removing it in the next iteration.