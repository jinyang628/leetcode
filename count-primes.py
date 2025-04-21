class Solution:
    def countPrimes(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 0
        isPrime = [True] * (n - 1)
        isPrime[0] = False
        ceil = math.ceil(math.sqrt(n)) + 1
        for i in range(1, ceil):
            for j in range(2 * i + 1, n - 1, i + 1):
                isPrime[j] = False
        res = 0
        for boolean in isPrime:
            if boolean:
                res += 1
        return res