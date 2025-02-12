class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        res = []
        length = len(nums)
        for i in range(length):
            popped = nums.pop(0)
            permutations = self.permute(nums)
            for p in permutations:
                p.append(popped)
            res.extend(permutations)
            nums.append(popped)
        return res