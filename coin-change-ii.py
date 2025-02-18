class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = [0] * (amount + 1)
        res[0] = 1
        for coin in coins:
            for i in range(coin, len(res)):
                res[i] += res[i - coin]
        return res[-1]