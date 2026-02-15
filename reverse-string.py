1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
45        """
6        left, right = 0, len(s) - 1
7        while left <= right:
8            s[left], s[right] = s[right], s[left]
9            left += 1
10            right -= 1
11        return s
12