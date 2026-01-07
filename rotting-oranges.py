1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        row, col = len(grid), len(grid[0])
5        queue = deque()
6        count = 0
7        for i in range(row):
8            for j in range(col):
9                if grid[i][j] == 1:
10                    count += 1
11                elif grid[i][j] == 2:
12                    queue.append((0, i, j))
13        if not count:
14            return 0
15        visited = set()
16        max_time = float('-inf')
17        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
18        while queue:
19            dist, x, y = queue.popleft()
20            if (x, y) in visited:
21                continue
22            if x < 0 or x >= row or y < 0 or y >= col:
23                continue
24            if grid[x][y] == 0:
25                continue
26            visited.add((x,y))
27            if grid[x][y] == 1:
28                max_time = max(max_time, dist)
29                count -= 1
30            for dx, dy in directions:
31                new_x, new_y = x + dx, y + dy
32                queue.append((dist + 1, new_x, new_y))
3334        if count:
35            return -1
36        return max_time
3738