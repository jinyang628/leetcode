1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        if len(s3) != len(s1) + len(s2):
4            return False
5        cache = {}
6        def helper(s1_idx: int, s2_idx: int, s3_idx: int) -> bool:
7            if s1_idx == len(s1) and s2_idx == len(s2) and s3_idx == len(s3):
8                return True
9            if (s1_idx, s2_idx) in cache:
10                return cache[(s1_idx, s2_idx)]
11            res = False
12            if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
13                res = res or helper(s1_idx + 1, s2_idx, s3_idx + 1)
14            if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
15                res = res or helper(s1_idx, s2_idx + 1, s3_idx + 1)
16            cache[(s1_idx, s2_idx)] = res
17            return res
18        return helper(0, 0, 0)
19