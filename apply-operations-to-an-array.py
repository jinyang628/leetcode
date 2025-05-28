class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        left = right = None
        for i in range(len(nums)):
            if not nums[i]:
                left = right = i
                while right < len(nums) and nums[right] == 0:
                    right += 1
                break
        if left == None:
            return nums
        while right < len(nums) and left < len(nums):
            nums[left], nums[right] = nums[right], nums[left]
            while right < len(nums) and nums[right] == 0:
                right += 1
            left += 1
        return nums