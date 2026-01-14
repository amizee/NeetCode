class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                right, left = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(left + right)
                elif t == "-":
                    stack.append(left - right)
                elif t == "*":
                    stack.append(left * right)
                elif t == "/":
                    stack.append(int(left / right))
        return stack[0]
        
# Intuition: stack stores the two operands and maintains the correct order