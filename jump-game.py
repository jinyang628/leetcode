class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPossibleIdx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= lastPossibleIdx:
                lastPossibleIdx = i
        return lastPossibleIdx == 0