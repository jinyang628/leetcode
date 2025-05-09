class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        memo = {}
        def dfs(idx: int, parity: int) -> int:
            if (idx, parity) in memo:
                return memo[(idx, parity)]
            if idx == len(nums):
                return 0
            curr_parity = nums[idx] % 2
            memo[(idx, parity)] = max(
                dfs(idx + 1, parity),
                nums[idx] + dfs(idx + 1, curr_parity) + (0 if curr_parity == parity else -1 * x)
            )
            return memo[(idx, parity)]
        return dfs(0, nums[0] % 2)