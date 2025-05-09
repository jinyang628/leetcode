class Solution:
    def countElements(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        return sum(1 for i in nums if smallest < i < largest)