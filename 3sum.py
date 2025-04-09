class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        left = 0
        print(nums)
        while left < len(nums) - 2:
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                if curr_sum <= 0:
                    while mid + 1 < right and nums[mid + 1] == nums[mid]:
                        mid += 1
                    mid += 1
                else:
                    while right - 1 > mid and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
            while left < len(nums) - 2 and nums[left + 1] == nums[left]:
                left += 1
            left += 1
        return res