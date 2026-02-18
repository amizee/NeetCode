from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        currSubstrs, res = [], []

        def isValidPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(j, i):
            if i >= len(s):
                if i == j:
                    res.append(currSubstrs.copy())
                return

            if isValidPalindrome(j, i):
                currSubstrs.append(s[j : i + 1])
                backtrack(i + 1, i + 1)
                currSubstrs.pop()
          
            backtrack(j, i + 1)

        backtrack(0, 0)
        return res

# Intuition: combinations style question.
# 2^n possible partitions because there's two choices - the current substring is a palindrome so we partition and start a new substring or skip partitioning.
# Base case: if we've reached the end of the string and both pointers are at the end (since otherwise this means we couldn't find a palindrome at the end and a pointer has been left behind)
# Use array.copy() when adding valid solutions (always for backtracking problems)
