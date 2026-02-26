1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x == 1:
4            return 1
5        left, right = 1, x // 2
6        while left <= right:
7            mid = left + (right - left) // 2
8            square = mid ** 2
9            if square == x:
10                return mid
11            elif square > x:
12                right = mid - 1
13            else:
14                left = mid + 1
15        return right
16171819