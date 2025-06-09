class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        res = True
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                res = False
        if res:
            return res
        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True