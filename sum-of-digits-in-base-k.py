class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits = []
        while n:
            remainder = n % k
            digits.append(remainder)
            n -= remainder
            n //= k
        return sum(digits)