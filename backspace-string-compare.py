1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        s_stack = []
4        t_stack = []
5        for char in s:
6            if char == "#":
7                if s_stack:
8                    s_stack.pop()
9            else:
10                s_stack.append(char)
11        for char in t:
12            if char == "#":
13                if t_stack:
14                    t_stack.pop()
15            else:
16                t_stack.append(char)
1718        return "".join(s_stack) == "".join(t_stack)