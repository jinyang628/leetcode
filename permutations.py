1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        length = len(nums)
4        if length == 1:
5            return [[nums[0]]]
6        res = []
7        for _ in range(length):
8            top = nums.pop(0)
9            subsets = self.permute(nums)
10            for subset in subsets:
11                subset.append(top)
12                res.append(subset)
13            nums.append(top)
14        return res