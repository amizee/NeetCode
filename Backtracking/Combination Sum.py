class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

# Intuition: Use the same number as many times as possible, and when you go over the target backtrack (by popping the number you just added) and try the other numbers.
# This way, you'll eventually test out every valid frequency for each number as a combination.
# By sorting the numbers when the current total goes over the target, you can return from this path and prevent unneccesary work.