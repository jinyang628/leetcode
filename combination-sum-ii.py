class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(idx: int, subset: list[int], total: int):
            print(idx, subset, total)
            if total == target:
                res.append(subset[:])
                return
            elif total > target or idx >= len(candidates):
                return 
            subset.append(candidates[idx])
            backtrack(idx + 1, subset, total + candidates[idx])
            subset.pop()
            current = candidates[idx]
            while idx < len(candidates) - 1 and candidates[idx + 1] == current:
                idx += 1
            backtrack(idx + 1, subset, total)
        backtrack(0, [], 0)
        return res