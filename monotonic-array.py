class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def isIncreasing(lst: list[int]) -> bool:
            if len(lst) <= 1:
                return True
            for i in range(1, len(nums)):
                if nums[i] >= nums[i - 1]:
                    continue
                return False
            return True
        def isDecreasing(lst: list[int]) -> bool:
            if len(lst) <= 1:
                return True
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    continue
                return False
            return True
        return isIncreasing(nums) or isDecreasing(nums)