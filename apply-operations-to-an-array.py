class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        res = []
        count = 0
        for num in nums:
            if num:
                res.append(num)
            else:
                count += 1
        res.extend([0] * count)
        return res