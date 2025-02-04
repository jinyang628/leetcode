class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if (sum(matchsticks)) % 4 != 0:
            return False
        length = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        def backtrack(idx: int) -> bool:
            if idx == len(matchsticks):
                for side in sides:
                    if side != length:
                        return False
                return True
            for i in range(len(sides)):
                if sides[i] + matchsticks[idx] <= length:
                    sides[i] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
                if sides[i] == 0:
                    return False
        return backtrack(0)