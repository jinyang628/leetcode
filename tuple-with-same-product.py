from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        track = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                res += track[product] * 8
                track[product] += 1
        return res