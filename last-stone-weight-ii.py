1class Solution:
2    def lastStoneWeightII(self, stones: List[int]) -> int:
3        total = sum(stones)
4        target = math.ceil(total / 2)
5        cache = {} # (idx, curr)
6        def dfs(idx: int, curr: int) -> int:
7            if (idx, curr) in cache:
8                return cache[(idx, curr)]
9            if curr > target:
10                return abs(curr - (total - curr))
11            if idx >= len(stones):
12                return abs(curr - (total - curr))
13            curr += stones[idx]
14            take = dfs(idx + 1, curr)
15            curr -= stones[idx]
16            skip = dfs(idx + 1, curr)
17            res = min(take, skip)
18            cache[(idx, curr)] = res
19            return res
20        return dfs(0, 0)
21