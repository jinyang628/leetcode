1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4        def dfs(idx: int, remainder: int, path: list[int]) -> None:
5            if not remainder:
6                res.append(path[:])
7                return 
89            if idx == len(candidates) or remainder < 0:
10                return
1112            path.append(candidates[idx])
13            dfs(idx, remainder - candidates[idx], path)
14            path.pop()
15            dfs(idx + 1, remainder, path)
1617        dfs(0, target, [])
18        return res