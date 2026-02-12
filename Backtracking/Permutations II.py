class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permsSet = set()
        
        def helper(i, nums):   
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = helper(i + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    if tuple(pCopy) not in permsSet:
                        resPerms.append(pCopy)
                    permsSet.add(tuple(pCopy))
            return resPerms
        
        return helper(0, nums)
        
# Intuition: check that each permutation doesn't already exist using a hashset before adding it to the result.