1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        members = set(nums)
4        res = []
5        for i in range(1, len(nums) + 1):
6            if i not in members:
7                res.append(i)
8        return res