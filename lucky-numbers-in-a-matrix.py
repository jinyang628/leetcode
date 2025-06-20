class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        mins = [float('inf')] * row
        maxs = [0] * col
        for i in range(row):
            for j in range(col):
                mins[i] = min(mins[i], matrix[i][j])
                maxs[j] = max(maxs[j], matrix[i][j])
        total = []
        track = set(maxs)
        for num in mins:
            if num in track:
                total.append(num)
        return total