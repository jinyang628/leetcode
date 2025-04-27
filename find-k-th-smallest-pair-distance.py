class Solution:
    def getNumPairs(self, dist: int, nums: list) -> int:
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > dist:
                left += 1
            count += right - left  # all pairs (left to right-1) are valid
        return count
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            num_pairs = self.getNumPairs(mid, nums)
            if num_pairs < k:
                left = mid + 1
            else:
                right = mid
        return left