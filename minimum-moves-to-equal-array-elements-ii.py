class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median_value = nums[len(nums) // 2]
        res = 0
        for num in nums:
            res += abs(num - median_value)
        return res