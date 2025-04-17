class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(len(prices) + 1)]
        for i in range(len(prices) - 1, -1, -1):
            for can_buy in range(2):
                for transactions_left in range(1, k + 1):
                    if can_buy:
                        dp[i][can_buy][transactions_left] = max(
                            -prices[i] + dp[i + 1][0][transactions_left],
                            dp[i + 1][can_buy][transactions_left]
                        )  
                    else:
                        dp[i][can_buy][transactions_left] = max(
                            prices[i] + dp[i + 1][1][transactions_left - 1],
                            dp[i + 1][can_buy][transactions_left]
                        )
        return dp[0][1][k]