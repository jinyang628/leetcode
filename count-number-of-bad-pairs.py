from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        """
        track = defaultdict(int)  
        good = 0
        for i in range(len(nums)):
            delta = nums[i] - i
            good += track[delta]
            track[delta] += 1  
        length = len(nums)
        return (length * (length - 1)) // 2 - good