class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1, int(n**0.5) + 1):
            if n % i != 0:
                continue
            res.append(i)
            k -= 1
            if k == 0:
                return i
        for num in res.copy()[::-1]:
            if num ** 2 == n:
                continue 
            k -= 1
            if k == 0:
                return n // num
        return -1