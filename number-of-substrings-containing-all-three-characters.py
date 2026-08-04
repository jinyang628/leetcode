1class Solution:
2    def numberOfSubstrings(self, s: str) -> int:
3        res = 0
4        left = right = 0
5        counter = Counter()
6        while right < len(s):
7            counter[s[right]] += 1
8            while counter["a"] > 0 and counter["b"] > 0 and counter["c"] > 0:
9                res += len(s) - right
10                counter[s[left]] -= 1
11                left += 1
12            right += 1
13        return res