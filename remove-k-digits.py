from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque([])
        for char in num:
            if not stack or int(stack[-1]) <= int(char):
                stack.append(char)
            elif k > 0:
                while k and stack and int(stack[-1]) > int(char):
                    k -= 1
                    stack.pop()
                stack.append(char)
            else:
                stack.append(char)
        while stack and stack[0] == "0":
            stack.popleft()
        print(k, stack)
        while k and stack:
            stack.pop()
            k -= 1
        return "".join(stack) if stack else "0"