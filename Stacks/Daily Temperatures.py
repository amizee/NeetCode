# My solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, 0, -1):
            if temperatures[i - 1] < temperatures[i]:
                res[i - 1] = 1
            elif temperatures[i - 1] >= temperatures[i]:
                while stack:
                    temp, index = stack[-1][0], stack[-1][1]
                    if temperatures[i - 1] < temp:
                        res[i - 1] = index - (i - 1)
                        break
                    stack.pop()
            stack.append((temperatures[i], i))
        return res
# Intuition: loop in reverse, always adding the current temp and its index to the stack. If the temp on the day before is less, then the res must be 1. Else, we go through the stack until we find a temp higher than the temp on the day before and calculate res if we find one, else leave it as 0.

# Cleaner solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

# Intuition: The stack contains temperatures that haven't found a warmer temperature yet. If we find a temp higher than the most recent day (i.e. top of the stack), then we calculate res for every day lower than this temp and pop it off the stack.