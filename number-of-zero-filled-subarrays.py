from collections import defaultdict
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # 1 zero -> 1
        # 2 zero -> 3
        # 3 zero -> 6
        # 4 zero -> 10
        # (n * (n + 1)) // 2
        i = runningZeros = 0
        track = defaultdict(int)
        while i < len(nums):
            if nums[i]:
                track[runningZeros] += 1
                runningZeros = 0
            else:
                runningZeros += 1
            i += 1
        if runningZeros:
            track[runningZeros] += 1
        res = 0
        for key, qty in track.items():
            if not key:
                continue
            res += qty * ((key * (key + 1)) // 2)
        return res