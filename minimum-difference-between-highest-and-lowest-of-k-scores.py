class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        res = float('inf')
        right = k - 1
        while right < len(nums):
            res = min(res, nums[right] - nums[left])
            left += 1
            right += 1
        return res