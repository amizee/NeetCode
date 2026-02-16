from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

# Intuition: input array contains duplicates but can only be used once to sum to the target.
# If you decide not to use a number, loop past all duplicates of this number at the same recursion level.
# e.g. [1, 1, 2], target = 3
# DFS decisions at index 0: Pick first 1 → later pick 2 → [1,2]
#Skip first 1 → move to second 1 → pick 1 → pick 2 → [1,2] AGAIN