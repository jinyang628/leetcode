1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5        def dfs(idx: int, subset: list[int]) -> None:
6            if idx == len(nums):
7                res.append(subset[:])
8                return
910            # take
11            subset.append(nums[idx])
12            dfs(idx + 1, subset)
13            subset.pop()
1415            # leave
16            idx += 1
17            while idx < len(nums) and nums[idx] == nums[idx - 1]:
18                idx += 1
19            dfs(idx, subset)
2021        dfs(0, [])
22        return res