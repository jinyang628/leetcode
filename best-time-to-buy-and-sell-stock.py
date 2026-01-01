1class Solution(object):
2    def maxProfit(self, prices):
3        """
456        """
7        maxSoFar = 0
8        minSoFar = prices[0]
9        for price in prices:
10            minSoFar = min(minSoFar, price)
11            maxSoFar = max(maxSoFar,price - minSoFar)
1213        return maxSoFar
1415