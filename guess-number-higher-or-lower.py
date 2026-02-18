1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
78class Solution:
9    def guessNumber(self, n: int) -> int:
10        left, right = 1, n
11        while left <= right:
12            mid = left + (right - left) // 2
13            res = guess(mid)
14            if res == 0:
15                return mid
16            elif res == -1:
17                right = mid - 1
18            else:
19                left = mid + 1
20