class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx: int, path: list):
            if idx == len(nums):
                res.append(path[:])
                return 
            path.append(nums[idx])
            backtrack(idx + 1, path)
            while idx < len(nums) - 1 and nums[idx + 1] == nums[idx]:
                idx += 1
            path.pop()
            backtrack(idx + 1, path)
        backtrack(0, [])
        return res