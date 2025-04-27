class Solution:
    def getNumPairs(self, nums: list[int], dist: int):
        left = count = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > dist:
                left += 1
            count += right - left
        return count
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            num_pairs = self.getNumPairs(nums, mid)
            if num_pairs < k:
                left = mid + 1
            else:
                right = mid
        return left