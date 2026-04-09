1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x = str(x)
4        left, right = 0, len(x) - 1
5        while left < right:
6            if x[left] != x[right]:
7                return False
8            left += 1
9            right -= 1
10        return True