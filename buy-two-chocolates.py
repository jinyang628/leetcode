1class Solution:
2    def buyChoco(self, prices: List[int], money: int) -> int:
3        prices.sort()
4        leftover = money - prices[0] - prices[1]
5        if leftover >= 0:
6            return leftover
7        else:
8            return money