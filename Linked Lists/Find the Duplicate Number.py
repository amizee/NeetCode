class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                return abs(nums[i])
            nums[index] *= -1

# Intuition: negative marking - loop through every number and set nums[number - 1] to negative. If there's a duplicate, the number at this index will already be negative, and you can return this number.
# O(n) time and O(1) space complexity

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# There's a linked list solution but I don't like it because it relies on some unintuitive math. You can treat the array as a linked list where each index represents the index that it points to next.
# Using fast and slow pointers, if there's a cycle the two pointers will eventually meet. From this pointer, running the fast and slow algorithm again will find the duplicate where the two pointers meet.