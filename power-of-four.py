1class Solution:
2    def isPowerOfFour(self, n: int) -> bool:
3        if n <= 0:
4            return False
56        while n % 4 == 0:
7            n //= 4
8        return n == 1
9