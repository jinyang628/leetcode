class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 != 0:
                n -= 1
                res += n // 2
                n //= 2 
                n += 1
            else:
                res += n // 2
                n //= 2 
        return res