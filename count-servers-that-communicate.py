1class Solution:
2    def countServers(self, grid: List[List[int]]) -> int:
3        visited = set()
4        res = 0
5        row, col = len(grid), len(grid[0])
6        for i in range(row):
7            for j in range(col):
8                if (i, j) in visited:
9                    continue
10                if grid[i][j] == 0:
11                    continue  
12                visited.add((i, j))
13                exists_neighbor_server = False
14                for r in range(i + 1, row):
15                    if grid[r][j] == 1:
16                        exists_neighbor_server = True
17                        if (r, j) not in visited:
18                            res += 1
19                    visited.add((r, j))
20                for r in range(i - 1, -1, -1):
21                    if grid[r][j] == 1:
22                        exists_neighbor_server = True
23                        if (r, j) not in visited:
24                            res += 1
25                    visited.add((r, j))
26                for c in range(j + 1, col):
27                    if grid[i][c] == 1:
28                        exists_neighbor_server = True
29                        if (i, c) not in visited:
30                            res += 1
31                    visited.add((i, c))
32                for c in range(j - 1, -1, -1):
33                    if grid[i][c] == 1:
34                        exists_neighbor_server = True
35                        if (i, c) not in visited:
36                            res += 1
37                    visited.add((i, c))
38                if exists_neighbor_server:
39                    print(i, j)
40                    res += 1
41        return res