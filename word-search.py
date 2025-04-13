class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or c < 0 or r >= row or c >= col:
                return False
            if board[r][c] == "*":
                return False
            if board[r][c] != word[idx]:
                return False
            tmp = board[r][c]
            board[r][c] = "*"
            res = dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c - 1, idx + 1) or dfs(r, c + 1, idx + 1)
            board[r][c] = tmp
            return res
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False