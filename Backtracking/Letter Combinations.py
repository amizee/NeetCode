from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def dfs(i, currStr):
            if i == len(digits):
                res.append(currStr)
                return

            letters = letterMap[digits[i]]
            for j in range(len(letters)):
                dfs(i + 1, currStr + letters[j])

        if digits:
            dfs(0, "")
        return res