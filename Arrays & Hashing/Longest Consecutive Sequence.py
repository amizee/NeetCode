class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        res = 0
        currLength = 1
        for n in numsSet:
            if n - 1 not in numsSet:
                currLength = 1
                while n + 1 in numsSet:
                    currLength += 1
                    n += 1
                res = max(res, currLength)
        return res

# Intuition: only consider numbers that can be the start of the sequence by checking if the number before it exists using a hashset for O(1) time.
# Always consider the opposite case!!!! (checking n - 1 instead of n + 1 solved this problem)