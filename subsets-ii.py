class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(idx: int, path: list[int]):
            if idx == len(nums):
                res.append(path[:])
                return
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()
            idx += 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1
            backtrack(idx, path)
        backtrack(0, [])
        return res