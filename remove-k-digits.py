from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque([])
        for char in num:
            while k and stack and int(stack[-1]) > int(char):
                k -= 1
                stack.pop()
            stack.append(char)
        while stack and stack[0] == "0":
            stack.popleft()
        while k and stack:
            stack.pop()
            k -= 1
        return "".join(stack) if stack else "0"