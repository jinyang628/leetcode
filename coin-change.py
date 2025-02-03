class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [amount + 1] * (amount + 1)
        amounts[0] = 0
        for i in range(1, len(amounts)):
            for coin in coins:
                if i - coin >= 0:
                    amounts[i] = min(
                        amounts[i - coin] + 1,
                        amounts[i]
                    )
        return amounts[-1] if amounts[-1] != (amount + 1) else -1