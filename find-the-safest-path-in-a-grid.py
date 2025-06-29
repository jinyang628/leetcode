from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        mat = [[-1] * col for _ in range(row)]
        queue = deque([]) # r, c, dist
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        while queue:
            r, c, dist = queue.popleft()
            if r < 0 or r >= row or c < 0 or c >= col: # invalid
                continue
            if mat[r][c] != -1: # visited
                continue
            mat[r][c] = dist
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = dr + r, dc + c
                queue.append((new_r, new_c, dist + 1))
        heap = [(-mat[0][0], 0, 0)]
        visited = set()
        while heap:
            negative_dist, r, c = heapq.heappop(heap)
            if r == row - 1 and c == col - 1:
                return -negative_dist
            if (r,c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = dr + r, dc + c
                if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col: # invalid
                    continue
                if (new_r, new_c) in visited:
                    continue
                heapq.heappush(heap, (-min(-negative_dist, mat[new_r][new_c]), new_r, new_c))