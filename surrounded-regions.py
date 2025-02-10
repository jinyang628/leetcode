class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        """
        row, col = len(board), len(board[0])
        def dfs(r: int, c: int):
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            if board[r][c] == "G":
                return 
            if board[r][c] != "O":
                return
            board[r][c] = "G"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or i == row - 1 or j == col - 1:
                    dfs(i, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] != "G":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"