class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        for i in range(n):
            for j in range(n):
                if i < j < n - i - 1:
                    fruits[i][j] = 0
                if j < i < n - 1 - j:
                    fruits[i][j] = 0
        res = 0
        for i in range(n):
            res += fruits[i][i]
        for i in range(1, n):
            for j in range(i + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], fruits[i - 1][j], fruits[i - 1][j + 1] if j + 1 < n else 0
                )
        for j in range(1, n):
            for i in range(j + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], fruits[i][j - 1], fruits[i + 1][j - 1] if i + 1 < n else 0
                )
        return res + fruits[-1][-2] + fruits[-2][-1]