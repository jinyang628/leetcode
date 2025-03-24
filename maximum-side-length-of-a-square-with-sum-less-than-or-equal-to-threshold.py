class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row, col = len(mat) + 1, len(mat[0]) + 1
        res = [[0] * col for _ in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                res[i][j] = res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + mat[i - 1][j - 1]
        def containsLEQ(length: int) -> bool:
            for i in range(1, row - length + 1):
                for j in range(1, col - length + 1):
                    total = (
                        res[i + length - 1][j + length - 1] - 
                        res[i - 1][j + length - 1] - 
                        res[i + length - 1][j - 1] + 
                        res[i - 1][j - 1]
                    )
                    if total <= threshold:
                        return True
            return False
        left = 0
        right = min(row, col) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if containsLEQ(mid):
                left = mid +1
            else:
                right = mid - 1
        return right