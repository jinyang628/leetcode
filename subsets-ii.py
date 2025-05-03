class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(idx: int, path: list[int]):
            if idx == len(nums):
                res.append(path[:])
                return
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()
            curr = nums[idx]
            while idx < len(nums) and nums[idx] == curr:
                idx += 1
            backtrack(idx, path)
        backtrack(0, [])
        return res