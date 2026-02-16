from typing import List

# Time: O(n^2 * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(i, nums):   
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = helper(i + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    resPerms.append(pCopy)
            return resPerms
        
        return helper(0, nums)
# Intuition: recurse from the last number of nums and build each permutation by inserting this number into all available positions, and pass this list of permutations back up for the next number.
    
# Time: O(n^2 * n!)
def permutationsIterative(nums):
    perms = [[]]

    for n in nums:
        nextPerms = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                nextPerms.append(pCopy)
        perms = nextPerms
    return perms