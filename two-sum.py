class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in track:
                return [track[curr], i]
            track[target - curr] = i