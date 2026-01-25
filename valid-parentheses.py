1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        for char in s:
5            if char in ["(", "[", "{"]:
6                stack.append(char)
7            elif not stack:
8                return False
9            elif char == ")" and stack[-1] == "(":
10                stack.pop()
11            elif char == "]" and stack[-1] == "[":
12                stack.pop()
13            elif char == "}" and stack[-1] == "{":
14                stack.pop()
15            else:
16                return False
1718        return len(stack) == 0
19