import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed: int) -> bool:
            time = 0
            for num in piles:
                time += math.ceil(num / speed)
            return time <= h
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left