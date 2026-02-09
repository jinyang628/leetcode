1class Solution:
2    def numEnclaves(self, grid: List[List[int]]) -> int:
3        row, col = len(grid), len(grid[0])
4        def dfs(r: int, c: int) -> None:
5            if r < 0 or r >= row or c < 0 or c >= col:
6                return
7            if grid[r][c] == 0:
8                return
9            grid[r][c] = 0
10            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
11                new_r, new_c = r + dr, c + dc
12                dfs(new_r, new_c)
13        for i in range(row):
14            dfs(i, 0)
15            dfs(i, col - 1)            
16        for i in range(col):
17            dfs(0, i)
18            dfs(row - 1, i) 
1920        def dfs_count(r: int, c: int) -> int:
21            if (r, c) in visited:
22                return 0 
23            visited.add((r, c))
24            if grid[r][c] == 0:
25                return 0
26            return 1 + dfs_count(r + 1, c) + dfs_count(r - 1, c) + dfs_count(r, c + 1) + dfs_count(r, c - 1)
2728        res = 0
29        visited = set()
30        for i in range(1, row - 1):
31            for j in range(1, col - 1):
32                if grid[i][j] == 0:
33                    continue 
34                res += dfs_count(i, j)
35        print(grid)
36        return res
37383940