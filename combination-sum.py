class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx: int, sumSoFar: int, pathSoFar: list[int]):
            if idx == len(candidates):
                if sumSoFar == target:
                    res.append(pathSoFar[:])
                return
            if sumSoFar > target:
                return
            pathSoFar.append(candidates[idx])
            helper(idx, sumSoFar + candidates[idx], pathSoFar)
            pathSoFar.pop()
            helper(idx + 1, sumSoFar, pathSoFar)
        helper(0, 0, [])
        return res