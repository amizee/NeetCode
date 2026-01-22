class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [0] * len(nums), [0] * len(nums)
        output = []

        total = 1
        for i, n in enumerate(nums):
            total *= n
            prefix[i] = total
        
        total = 1
        for i, n in enumerate(reversed(nums)):
            total *= n
            suffix[len(nums) - i - 1] = total
        
        for i in range(len(nums)):
            if i == 0:
                output.append(suffix[i + 1])
            elif i == len(nums) - 1:
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * suffix[i + 1])
        return output

# Intuition: calculate the prefix and suffix sums, including the current index. To calculate output[i], multiple the prefix sum of elements before "i" and the suffix sum of elements after "i".