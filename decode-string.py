1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4        for i in range(len(s)):
5            if s[i] != "]":
6                stack.append(s[i])
7            else:
8                substr = ""
9                while stack and stack[-1] != "[":
10                    substr = stack.pop() + substr
11                stack.pop()
12                multiplier = ""
13                while stack and stack[-1].isdigit():
14                    multiplier = stack.pop() + multiplier
15                stack.append(int(multiplier) * substr)
16        return "".join(stack)