1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        left = 1
4        right = max(piles)
5        def canFinish(speed: int) -> bool:
6            res = 0
7            for pile in piles:
8                res += math.ceil(pile / speed)
9            return res <= h
10        while left <= right:
11            mid = left + (right - left) // 2
12            if canFinish(mid):
13                right = mid - 1
14            else:
15                left = mid + 1
16        return left
17