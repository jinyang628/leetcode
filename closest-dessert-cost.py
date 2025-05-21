from collections import defaultdict
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best = [None]
        def backtrack(costSoFar: int, toppings_track: dict, idx: int):
            if idx == len(toppingCosts) or costSoFar >= target:
                if best[0] is None or abs(target - costSoFar) < abs(target - best[0]):
                    best[0] = costSoFar
                if abs(target - costSoFar) == abs(target - best[0]):
                    best[0] = min(costSoFar, best[0])
                return
            if toppings_track[idx] == 2:
                backtrack(costSoFar, toppings_track, idx + 1)
            else:
                toppings_track[idx] += 1
                backtrack(costSoFar + toppingCosts[idx], toppings_track, idx)
                toppings_track[idx] -= 1
                backtrack(costSoFar, toppings_track, idx + 1)
        for base in baseCosts:
            backtrack(base, defaultdict(int), 0)
        return best[0]