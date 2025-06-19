from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque([(0,0,1)]) # x, y, dist 
        visited = set()
        row, col = len(grid) - 1, len(grid[0]) - 1
        while queue:
            x, y, dist = queue.popleft()
            if (x, y) in visited:
                continue 
            if x == row and y == col:
                return dist
            visited.add((x,y))
            # add neighbors 
            dist += 1
            for dx, dy in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                curr_x, curr_y = dx + x, dy + y
                if curr_x < 0 or curr_x > row or curr_y < 0 or curr_y > col:
                    continue 
                if grid[curr_x][curr_y] == 1:
                    continue 
                queue.append((curr_x, curr_y, dist))
        return -1