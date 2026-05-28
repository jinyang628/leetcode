1class Solution:
2    def removeDuplicates(self, s: str, k: int) -> str:
3        stack = []
4        idx = -1
5        while idx < len(s) - 1:
6            idx += 1
7            if not stack:
8                stack.append((s[idx], 1))
9                continue
1011            prev_char, prev_count = stack[-1]
12            if prev_char == s[idx]:
13                if prev_count == k - 1:
14                    for _ in range(k - 1):
15                        stack.pop()
16                else:
17                    stack.append((s[idx], prev_count + 1))
18            else:
19                stack.append((s[idx], 1))
2021        print(stack)
22        res = []
23        for char, freq in stack:
24            res.append(char)
25        return "".join(res)