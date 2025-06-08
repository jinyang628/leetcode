class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def countPalindromes(left: int, right: int) -> int:
            if left < 0 or right >= len(s):
                return 0
            nonlocal count
            if s[left] != s[right]:
                return 0
            count += 1
            countPalindromes(left - 1, right + 1)
        for i in range(len(s)):
            countPalindromes(i, i)
            countPalindromes(i, i+1)
        return count