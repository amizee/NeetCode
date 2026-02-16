from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if openN > closedN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

# Intuition: build only valid parentheses combinations
# If you have n open and closed brackets, then you can add this combination.
# Open bracket always come first and can only be added if theres less than n and closed brackets can only be added if there's at least one more open bracket than closed brackets.
# To consider all combinations, always pop off the bracket you just added to the stack.
# If n = 3, starts with ((())) then pops off to get (( and checks the closed bracket conditional to get (() etc.