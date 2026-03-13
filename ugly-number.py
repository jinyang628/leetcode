1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n == 0:
4            return False
5        while n != 1:
6            chosen = False
7            for candidate in [2, 3, 5]:
8                if n % candidate == 0:
9                    chosen = True
10                    n //= candidate 
11            if not chosen:
12                return False
13        return True