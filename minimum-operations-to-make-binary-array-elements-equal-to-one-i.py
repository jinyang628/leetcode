class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left = count = 0
        length = len(nums)
        for i in range(length - 2):
            if nums[i] == 0:
                count += 1
                nums[i] = 1
                nums[i + 1] = 1 if not nums[i + 1] else 0
                nums[i + 2] = 1 if not nums[i + 2] else 0
        return -1 if not nums[length - 1] or not nums[length - 2] else count