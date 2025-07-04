class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        row = col = len(grid)
        totalSum = (1 + (row * col))*((row * col) / 2)
        visited = set()
        a = b = None
        runningSum = 0
        for i in range(row):
            for j in range(col):
                runningSum += grid[i][j]
                if grid[i][j] in visited:
                    a = grid[i][j]
                else:
                    visited.add(grid[i][j])
        b = totalSum - (runningSum - a)
        return [a, int(b)]