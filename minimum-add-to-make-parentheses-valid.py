class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)