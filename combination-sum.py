class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(set(candidates))
        res = []
        def backtrack(idx: int, path: list[int], sumSoFar: int):
            if idx == len(candidates):
                if sumSoFar == target:
                    res.append(path[:])
                return 
            if sumSoFar > target:
                return
            path.append(candidates[idx])
            backtrack(idx, path, sumSoFar + candidates[idx])
            path.pop()
            backtrack(idx + 1, path, sumSoFar)
        backtrack(0, [], 0)
        return res