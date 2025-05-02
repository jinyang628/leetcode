class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            print(char, stack)
            if not stack:
                stack.append(char)
            elif stack[-1] != char and (stack[-1] == char.upper() or stack[-1] == char.lower()):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)