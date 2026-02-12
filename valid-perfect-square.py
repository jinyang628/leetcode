1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        if num == 1:
4            return True
5        left, right = 0, num // 2
6        while left <= right:
7            mid = left + (right - left) // 2
8            square = mid ** 2
9            if square == num:
10                return True
11            elif square < num:
12                left = mid + 1
13            else:
14                right = mid - 1
15        return False
16