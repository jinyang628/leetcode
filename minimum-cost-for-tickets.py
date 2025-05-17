class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        first_day, last_day = min(days), max(days)
        length = last_day - first_day + 1
        dp = [0] * (length + 1)
        idx = 0
        actual_days = set(days)
        for i in range(1, len(dp)):
            day = i + first_day  - 1
            if day not in actual_days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )
                idx += 1
        return dp[-1]