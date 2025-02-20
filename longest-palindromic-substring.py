class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        def longestPalindrome(left: int, right: int) -> int:
            if left < 0 or right >= len(s):
                return s[left + 1: right]
            if s[left] != s[right]:
                return s[left + 1: right]
            return longestPalindrome(left - 1, right + 1)
        for i in range(len(s) - 1):
            first = longestPalindrome(i, i)
            second = longestPalindrome(i, i + 1)
            print(first, second)
            if len(first) > len(res):
                res = first
            if len(second) > len(res):
                res = second
        return res