class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                substring = []
                while stack[-1] != "(":
                    substring.append(stack.pop()[::-1])
                    pass
                stack.pop()
                stack.append("".join(substring))
            else:
                stack.append(char)
        return "".join(stack)