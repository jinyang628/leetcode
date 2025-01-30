class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(idx: int, candidates: list[int]):
            if idx == n + 1:
                if len(candidates) == k:
                    res.append(candidates[:])
                return
            candidates.append(idx)
            backtrack(idx + 1, candidates)
            candidates.pop()
            backtrack(idx + 1, candidates)
        backtrack(1, [])
        return res