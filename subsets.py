class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(lst: list[int], idx: int):
            if idx == len(nums):
                res.append(lst[:])
                return
            lst.append(nums[idx])
            backtrack(lst, idx + 1)
            lst.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(lst, idx + 1)
        backtrack([], 0)
        return res