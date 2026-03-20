class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

# Intuition: start from the goal and see if you can find a point you can reach from by looping in reverse.
# If so, set the goal to that point and repeat.