1class Solution:
2    def coloredCells(self, n: int) -> int:
3        if n == 1:
4            return 1
5        # 4 8 12
6        # increments incremented by 4
7        n -= 1
8        total_increments = int((n / 2) * (4 + 4 + (4 * (n - 1))))
9        return total_increments + 1