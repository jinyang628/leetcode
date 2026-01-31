1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        row, col = len(board), len(board[0])
4        def dfs(r: int, c: int, idx: int, visited: set) -> bool:
5            if idx == len(word):
6                return True
7            if r < 0 or r >= row or c < 0 or c >= col:
8                return False
9            if (r, c) in visited:
10                return False
11            if board[r][c] != word[idx]:
12                return False
13            visited.add((r, c))
1415            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
16                new_x, new_y = dx + r, dy + c
17                if dfs(new_x, new_y, idx + 1, visited):
18                    return True
1920            visited.remove((r, c))
21            return False
22        for i in range(row):
23            for j in range(col):
24                if dfs(i, j, 0, set()):
25                    return True
26        return False
2728