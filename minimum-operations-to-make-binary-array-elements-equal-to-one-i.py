class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 1:
                continue
            nums[i] = 0 if nums[i] else 1
            nums[i + 1] = 0 if nums[i + 1] else 1
            nums[i + 2] = 0 if nums[i + 2] else 1
            count += 1
        if nums[len(nums) - 2] and nums[len(nums) - 1]:
            return count
        return -1