1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left, right = 0, len(s) - 1
45        while left < right:
6            if not s[left].isalnum():
7                left += 1
8                continue
9            if not s[right].isalnum():
10                right -= 1
11                continue
12            if s[left].lower() != s[right].lower():
13                return False
14            left += 1
15            right -= 1
16        return True
17