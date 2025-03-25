from collections import Counter
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        track = Counter(nums)
        res = 0
        for key, _ in track.items():
            if key < 0:
                continue
            res += key
        if res:
            return res
        return res if res in track else max(nums)