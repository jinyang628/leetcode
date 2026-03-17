1class Solution:
2    def smallestNumber(self, pattern: str) -> str:
3        visited = set()
4        ans = None
5        def backtrack(idx: int, curr: int, path: list[int], visited: set) -> None:
6            nonlocal ans
7            if ans:
8                return 
9            if idx == len(pattern):
10                path = [str(i) for i in path]
11                ans = "".join(path)
12                return 
1314            original = curr
15            while pattern[idx] == "I" and curr <= 9:
16                curr += 1
17                if curr in visited:
18                    continue
19                path.append(curr)
20                visited.add(curr)
21                backtrack(idx + 1, curr, path, visited)
22                path.pop()
23                visited.remove(curr)
24            while pattern[idx] == "D" and curr > 1:
25                curr -= 1
26                if curr in visited:
27                    continue
28                path.append(curr)
29                visited.add(curr)
30                backtrack(idx + 1, curr, path, visited)
31                path.pop()
32                visited.remove(curr)
3334        for i in range(1, 10):
35            if not ans:
36                backtrack(0, i, [i], {i})
3738        return ans