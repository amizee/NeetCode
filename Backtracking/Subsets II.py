from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currSet, subsets = [], []
        self.helper(0, nums, currSet, subsets)
        return subsets
    
    def helper(self, i, nums, currSet, subsets):
        if i == len(nums):
            subsets.append(currSet.copy())
            return subsets
        
        currSet.append(nums[i])
        self.helper(i + 1, nums, currSet, subsets)
        currSet.pop()

        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, currSet, subsets)

# Intuition: slight variation from the normal subsets problem. At each step, when we exclude a number loop until the next non-duplicate number.
# This prevents duplicates because subsets formed by excluding a value only occur once (i.e. each path contains a distinct number of duplicates so if there were 2 2s there would be a path each with 0, 1 and 2 2s)