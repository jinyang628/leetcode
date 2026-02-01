1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        tracker = {}
4        def backtrack(idx: int, remainder: int) -> int:
5            if idx == len(coins):
6                if not remainder:
7                    return 1
8                return 0
9            if (idx, remainder) in tracker:
10                return tracker[(idx, remainder)]
11            if remainder < 0:
12                return 0
13            take = backtrack(idx, remainder - coins[idx])
14            give = backtrack(idx + 1, remainder)
15            tracker[(idx, remainder)] = take + give
16            return take + give
1718        return backtrack(0, amount)
19