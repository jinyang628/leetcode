1class Solution:
2    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
3        row, col = len(img), len(img[0])
4        prefixSums = [[0] * col for _ in range(row)]
5        res = [[0] * col for _ in range(row)]
6        for i in range(row):
7            curr = 0
8            for j in range(col):
9                curr += img[i][j]
10                prefixSums[i][j] = curr
11        def calculateAverage(center_r: int, center_c: int) -> int:
12            nonlocal row
13            nonlocal col
14            first_row = max(0, center_r - 1)
15            last_row = min(row - 1, center_r + 1)
16            first_col = max(0, center_c - 1)
17            last_col = min(col - 1, center_c + 1)
18            ans = 0 
19            denominator = (last_row - first_row + 1) * (last_col - first_col + 1)
20            for r in range(first_row, last_row + 1):
21                ans += prefixSums[r][last_col] - (prefixSums[r][first_col - 1] if first_col > 0 else 0)
22            ans //= denominator
23            return ans
2425        for i in range(row):
26            for j in range(col):
27                res[i][j] = calculateAverage(i, j)
28        return res