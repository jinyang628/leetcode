1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        row, col = len(image), len(image[0])
4        visited = set()
5        def dfs(r: int, c: int, member: int, target: int) -> None:
6            if r < 0 or r >= row or c < 0 or c >= col:
7                return
8            if image[r][c] != member:
9                return
10            if (r, c) in visited:
11                return
12            visited.add((r, c))
13            image[r][c] = target
14            dfs(r - 1, c, member, target)
15            dfs(r + 1, c, member, target)
16            dfs(r, c - 1, member, target)
17            dfs(r, c + 1, member, target)
1819        dfs(sr, sc, image[sr][sc], color)
20        return image
21