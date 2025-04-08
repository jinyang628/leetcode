class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(len(prices) + 1)]
        for idx in range(len(prices) - 1, -1, -1):
            for can_sell in range(2):
                for i in range(1, k + 1):
                    if can_sell:
                        dp[idx][can_sell][i] = max(
                            dp[idx + 1][can_sell][i], # dont sell today
                            prices[idx] + dp[idx + 1][0][i - 1] # sell today
                        )
                    else:
                        dp[idx][can_sell][i] = max(
                            dp[idx + 1][can_sell][i], # dont buy today
                            - prices[idx] + dp[idx + 1][1][i]# buy today
                        )
        return dp[0][0][k]