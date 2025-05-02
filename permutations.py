class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        res = []
        for _ in range(len(nums)):
            curr = nums.pop(0)
            wish = self.permute(nums)
            for p in wish:
                p.append(curr)
            res.extend(wish)
            nums.append(curr)
        return res