class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = carry = 0
        while numBottles:
            res += numBottles
            original = numBottles
            numBottles = (numBottles + carry) // numExchange
            carry = (original + carry) % numExchange
        return res