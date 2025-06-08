from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        track = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            track[nums[i]] += 1
            count += (track[nums[i]] - 1)
        return count