class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, subsets = [], []
        self.helper(0, nums, currSet, subsets)
        return subsets

    def helper(self, i, nums, currSet, subsets):
        if i == len(nums):
            subsets.append(currSet.copy())
            return subsets
        
        # Include nums[i]
        currSet.append(nums[i])
        self.helper(i + 1, nums, currSet, subsets)
        # Exclude nums[i]
        currSet.pop()
        self.helper(i + 1, nums, currSet, subsets)

# Intuition: To get all possible subsets, loop through the list of nums and at each num you can choose to include it or not, creating a decision tree branching by 2.
# When you've reached the bottom of the tree (i.e. end of nums) the subset will be complete and you can add it to "subsets" which acts a global variable because it is a list reference.
# The backtracking comes from popping from currSet, which excludes the most recent number.
# No duplicates because you don't look at all the nums at once, you only add a number as you go down the tree. (i.e. [1, 2] but it's impossible to get [2, 1] because 1 has been looked at already before 2)
# Time complexity: n * (2^n) so the height of the tree is n.