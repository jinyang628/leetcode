1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        def isPalindrome(substr: str) -> bool:
4            left, right = 0, len(substr) - 1
5            while left < right:
6                if substr[left] != substr[right]:
7                    return False
8                left += 1
9                right -= 1
10            return True
11        left, right = 0, len(s) - 1
12        seen_diff = False
13        while left < right:
14            if s[left] != s[right]:
15                if seen_diff:
16                    return False
17                return isPalindrome(s[left:right]) or isPalindrome(s[left + 1: right + 1])
18            left += 1
19            right -= 1
20        return True