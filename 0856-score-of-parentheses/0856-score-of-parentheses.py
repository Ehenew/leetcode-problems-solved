class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(1, 2 * v)        
        return stack.pop()