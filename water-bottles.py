class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = res = 0
        while numBottles > 0:
            res += numBottles
            empty += numBottles
            numBottles = empty // numExchange 
            empty = empty % numExchange
        return res