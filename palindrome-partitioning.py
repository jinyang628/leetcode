1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        track = {} # key is f"{start}{end}", value is boolean indicating whether its terue. 
4        def isPalindrome(left: int, right: int) -> bool:
5            key = f"{left}{right}"
6            if key in track:
7                return track[key]
8            substring = s[left: right + 1]
9            l, r = 0, len(substring) - 1
10            while l < r:
11                if substring[l] != substring[r]:
12                    track[key] = False
13                    return False
14                l += 1
15                r -= 1
16            track[key] = True
17            return True
1819        res = []
20        def backtrack(left: int, right: int, path: list[str]) -> None:
21            if right == len(s):
22                if left == len(s):
23                    res.append(path[:])
24                return
2526            if isPalindrome(left, right):
27                path.append(s[left: right + 1])
28                backtrack(right + 1, right + 1, path)
29                path.pop()
30            backtrack(left, right + 1, path) 
3132        backtrack(0, 0, [])
33        return res