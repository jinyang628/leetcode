1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
45        for char in tokens:
6            if char[-1].isdigit():
7                stack.append(int(char))
8                continue
9            first, second = stack.pop(), stack.pop()
10            if char == "+":
11                stack.append(second + first)
12            elif char == "-":
13                stack.append(second - first)
14            elif char == "*":
15                stack.append(second * first)
16            else:
17                res = second/first
18                if res < 0:
19                    stack.append(math.ceil(res))
20                else:
21                    stack.append(math.floor(res))
2223        return stack[0]