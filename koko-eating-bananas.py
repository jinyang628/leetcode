1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        minimum, maximum  = 1, max(piles)
45        def canFinish(speed: int, idx: int, timeLeft: int) -> bool:
6            if idx == len(piles) and timeLeft >= 0:
7                return True
8            if timeLeft <= 0:
9                return False
10            timeNeeded = math.ceil(piles[idx] / speed)
11            return canFinish(speed, idx + 1, timeLeft - timeNeeded)
1213        lastValidSpeed = None
14        while minimum <= maximum:
15            speed = minimum + (maximum - minimum) // 2
16            if canFinish(speed, 0, h):
17                lastValidSpeed = speed
18                maximum = speed - 1
19            else:
20                minimum = speed + 1
2122        return lastValidSpeed