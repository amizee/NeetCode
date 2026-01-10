class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = ["(", "{", "["]
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if c == ")" and bracket != "(":
                    return False
                if c == "}" and bracket != "{":
                    return False
                if c == "]" and bracket != "[":
                    return False
        if stack:
            return False
        return True
                    
# Intuition: Add open brackets to a stack in order, so when a closed bracket is found it must match the most recent open bracket.