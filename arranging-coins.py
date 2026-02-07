1class Solution:
2    def arrangeCoins(self, n: int) -> int:
3        left, right = 0, n
4        while left <= right:
5            mid = left + (right - left) // 2
6            if (mid / 2) * (1 + mid) <= n:
7                left = mid + 1
8            else:
9                right = mid - 1
10        return right