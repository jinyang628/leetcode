from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total = time = count = 0
        queue = deque([])
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        exit = False
        while not exit:
            tmp = deque([])
            while queue:
                r, c = queue.popleft()
                count += 1
                grid[r][c] = -1
                if r > 0 and grid[r - 1][c] == 1:
                    grid[r-1][c] = 2
                    tmp.append((r - 1, c))
                if r < row - 1 and grid[r + 1][c] == 1:
                    grid[r+1][c] = 2
                    tmp.append((r + 1, c))
                if c > 0 and grid[r][c - 1] == 1:
                    grid[r][c-1] = 2
                    tmp.append((r, c - 1))
                if c < col - 1 and grid[r][c + 1] == 1:
                    grid[r][c+1] = 2
                    tmp.append((r, c + 1))
            if not tmp:
                exit = True
            else:
                time += 1
                queue = tmp
        return time if total == count else -1