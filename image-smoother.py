class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        prefixSum = [[0] * (col + 2) for _ in range(row + 2)]
        for i in range(1, row + 2):
            for j in range(1, col + 2):
                if i < (row + 1) and j < (col + 1):
                    prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + img[i - 1][j - 1]
                else:
                    prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1]
        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                total = prefixSum[i + 2][j + 2]
                if (i - 1) >= 0:
                    total -= prefixSum[i - 1][j + 2]
                if (j - 1) >= 0:
                    total -= prefixSum[i + 2][j - 1]
                if (i - 1) >= 0 and (j - 1) >= 0:
                    total += prefixSum[i - 1][j - 1]
                divisor = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        curr_x, curr_y = i + dx, j + dy
                        if curr_x < 0 or curr_x >= row or curr_y < 0 or curr_y >= col:
                            continue
                        divisor += 1
                res[i][j] = math.floor(total / divisor)
        return res