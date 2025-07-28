class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = k - 1
        minSoFar = nums[k - 1] - nums[left]
        while right < len(nums) - 1:
            right += 1
            if right < k:
                continue
            left += 1
            minSoFar = min(minSoFar, nums[right] - nums[left])
        return minSoFar