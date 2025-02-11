class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific = [[None] * col for _ in range(row)]
        atlantic = [[None] * col for _ in range(row)]
        def dfs_pacific(r: int, c: int):
            if r < 0 or r >= row or c < 0 or c >= col:
                return 
            if pacific[r][c] != None:
                return 
            pacific[r][c] = True
            curr_height = heights[r][c]
            if r + 1 < row and heights[r + 1][c] >= curr_height:
                dfs_pacific(r + 1, c)
            if r - 1 >= 0 and heights[r - 1][c] >= curr_height:
                dfs_pacific(r - 1, c)
            if c + 1 < col and heights[r][c + 1] >= curr_height:
                dfs_pacific(r, c + 1)
            if c - 1 >= 0 and heights[r][c - 1] >= curr_height:
                dfs_pacific(r, c - 1)
        def dfs_atlantic(r: int, c: int):
            if r < 0 or r >= row or c < 0 or c >= col:
                return 
            if atlantic[r][c] != None:
                return 
            atlantic[r][c] = True
            curr_height = heights[r][c]
            if r + 1 < row and heights[r + 1][c] >= curr_height:
                dfs_atlantic(r + 1, c)
            if r - 1 >= 0 and heights[r - 1][c] >= curr_height:
                dfs_atlantic(r - 1, c)
            if c + 1 < col and heights[r][c + 1] >= curr_height:
                dfs_atlantic(r, c + 1)
            if c - 1 >= 0 and heights[r][c - 1] >= curr_height:
                dfs_atlantic(r, c - 1)
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    dfs_pacific(i, j)
                if i == row - 1 or j == col - 1:
                    dfs_atlantic(i, j)
        res = []
        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res