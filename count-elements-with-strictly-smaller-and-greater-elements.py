class Solution:
    def countElements(self, nums: List[int]) -> int:
        track = {}
        res = 0
        new_nums = sorted(nums)
        while len(new_nums) >= 2 and new_nums[0] == new_nums[1]:
            new_nums.pop(0)
        while len(new_nums) >= 2 and new_nums[-1] == new_nums[-2]:
            new_nums.pop()
        for i in range(len(new_nums)):
            track[new_nums[i]] = i
        for num in nums:
            if 0 < track[num] < len(new_nums) - 1:
                res += 1
        return res