class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        # split in middle
        def get_longest(i: int, j: int) -> str:
            if i < 0 or j >= len(s):
                return s[i + 1: j]
            if s[i] != s[j]:
                if i + 1 == j:
                    return s[i]
                return s[i + 1: j]
            return get_longest(i - 1, j + 1)
        for i in range(len(s) - 1):
            odd_palindrome = get_longest(i, i)
            even_palindrome = get_longest(i, i + 1)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome
            if len(even_palindrome) > len(res):
                res = even_palindrome
        return res