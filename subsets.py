class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subsetSoFar: list[int], idx: int):
            if idx == len(nums):
                res.append(subsetSoFar[:])
                return
            subsetSoFar.append(nums[idx])
            backtrack(subsetSoFar, idx + 1)
            subsetSoFar.pop()
            backtrack(subsetSoFar, idx + 1)
        backtrack([], 0)
        return res