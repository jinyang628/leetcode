class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        left = 0
        while left < len(nums) - 2:
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0:
                    res.append(
                        [nums[left], nums[mid], nums[right]]
                    )
                    mid += 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                elif total < 0:
                    mid += 1
                else:
                    right -= 1
            left += 1
            while left < len(nums) - 2 and nums[left] == nums[left - 1]:
                left += 1
        return res