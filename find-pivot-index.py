class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums) - nums[0]
        for i in range(len(nums) - 1):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i + 1]
        if left == right:
            return len(nums) - 1
        return -1