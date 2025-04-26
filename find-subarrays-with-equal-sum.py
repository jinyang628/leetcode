class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            sum = nums[i] + nums[i + 1]
            if sum in seen:
                return True
            seen.add(sum)
        return False