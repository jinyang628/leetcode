class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getNumDays(capacity: int) -> int:
            curr = 0
            res = 1
            for weight in weights:
                if curr + weight <= capacity:
                    curr += weight
                else:
                    curr = weight
                    res += 1
            return res
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            if getNumDays(mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left