import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, max(nums)
        def getResult(divisor: int) -> int:
            res = 0
            for num in nums:
                res += math.ceil(num / divisor)
            return res
        res = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            if not mid:
                left += 1
                continue
            if getResult(mid) <= threshold:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res