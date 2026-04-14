class Solution:
    def minOperations(self, s: str) -> int:
        n = s[::2].count('0') + s[1::2].count('1')
        return min(n, len(s) - n)