1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        res = [0] * (amount + 1)
4        res[0] = 1
5        for coin in coins:
6            for i in range(coin, len(res)):
7                res[i] += res[i - coin]
89        return res[-1]