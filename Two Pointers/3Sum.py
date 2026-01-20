class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums): # Fix one of the numbers
            if i > 0 and n == nums[i - 1]: # Handles duplicate "targets"
                continue

            l, r = i + 1, len(nums) - 1 # Can't reuse the same element in a triplet, we know that any triplets including numbers before i have already been found
            while l < r:
                threeSum = nums[l] + nums[r] + n
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]]) # Guaranteed to be unique already
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # Makes sure at least one of the numbers changes so no repeated triplets ([-2, 0, 0, 2, 2])
                        l += 1

        return res

# Intuition: loop through every number and then solve two-sum with that as the target. Requires lots of small details to prevent duplicates.
        