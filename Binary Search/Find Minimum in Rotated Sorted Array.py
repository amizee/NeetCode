class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1

# Intuition: if the current window is sorted, then the lower bound must be the minimum. Otherwise, it isn't sorted.
# This means that if the middle number is less than the rightmost number, the minimum is on the left (or is the middle). If it's more than the rightmost number, then this must be the rotated portion of the array and the minimum is on the right.
# Note: found this one tricky