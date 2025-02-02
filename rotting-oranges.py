from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        totalOranges = currRotten = 0
        queue = deque([])
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    totalOranges += 1
                    if grid[i][j] == 2:
                        queue.append((i, j, 0))
        if not totalOranges:
            return 0
        while queue:
            r, c, time = queue.popleft()
            if r < 0 or r >= row or c < 0 or c >= col:
                continue
            if grid[r][c] == 0:
                continue
            currRotten += 1
            if currRotten == totalOranges:
                return time
            grid[r][c] = 0
            queue.append((r - 1, c, time + 1))
            queue.append((r + 1, c, time + 1))
            queue.append((r, c - 1, time + 1))
            queue.append((r, c + 1, time + 1))
        return -1