class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(speed: int) -> int:
            timeNeeded =0
            for pile in piles:
                timeNeeded += math.ceil(pile / speed)
            return timeNeeded
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if eat(mid) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left