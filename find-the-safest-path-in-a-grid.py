from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        queue = deque([])
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        grid = [[float('inf')] * col for _ in range(row)]
        while queue:
            x, y, dist = queue.popleft()
            if x < 0 or x >= row or y < 0 or y >= col:
                continue 
            if grid[x][y] != float('inf'):
                continue 
            grid[x][y] = dist
            queue.append((x + 1, y, dist + 1))
            queue.append((x - 1, y, dist + 1))
            queue.append((x, y - 1, dist + 1))
            queue.append((x, y + 1, dist + 1))
        heap = [(-grid[0][0],0,0)]
        visited = set()
        while heap:
            negative_dist, x, y = heapq.heappop(heap)
            if x == row - 1 and y == col - 1:
                return -negative_dist
            if (x, y) in visited:
                continue
            visited.add((x,y))
            for d_x, d_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + d_x, y + d_y
                if 0 <= new_x < row and 0 <= new_y < col:
                    heapq.heappush(heap, (max(-grid[new_x][new_y], negative_dist), new_x, new_y))