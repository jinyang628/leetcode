class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def dfs(idx: int, step: int, path: dict, is_positive: bool) -> bool:
            if (nums[idx] > 0 and not is_positive) or (nums[idx] < 0 and is_positive):
                return False
            if idx in path:
                if step - path[idx] > 1:
                    return True
                return False
            path[idx] = step
            return dfs(
                (idx + nums[idx] % len(nums)) % len(nums),
                step + 1,
                path,
            ) 
        for i in range(len(nums)): 
            if dfs(i, 0, {}, nums[i] > 0):
                return True
        return False