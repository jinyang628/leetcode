class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx: int, path: list[int], sumSoFar: int) -> None:
            if sumSoFar == target:
                res.append(path[:])
                return 
            if sumSoFar > target:
                return 
            if idx == len(candidates):                    
                return 
            path.append(candidates[idx])
            helper(idx, path, sumSoFar + candidates[idx])
            path.pop()
            helper(idx + 1, path, sumSoFar)
        helper(0, [], 0)
        return res