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
                print(currSubstrs.copy())
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
