class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        lastIdxReached = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= lastIdxReached:
                lastIdxReached = i
        return lastIdxReached == 0