1class Solution:
2    def scoreOfString(self, s: str) -> int:
3        res = 0
4        for i in range(len(s) - 1):
5            res += abs(ord(s[i]) - ord(s[i + 1]))
6        return res