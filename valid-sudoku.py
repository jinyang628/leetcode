class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = len(board), len(board[0])
        def compare_square(r: int, c: int) -> bool:
            track = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    curr = board[i][j]
                    if curr ==".":
                        continue
                    if curr in track:
                        return False
                    track.add(curr)
            return True
        def compare_row(r: int) -> bool:
            track = set()
            for i in range(col):
                curr = board[r][i]
                if curr == ".":
                    continue
                if curr in track:
                    return False
                track.add(curr)
            return True
        def compare_col(c: int) -> bool:
            track = set()
            for i in range(row):
                curr = board[i][c]
                if curr == ".":
                    continue
                if curr in track:
                    return False
                track.add(curr)
            return True
        for i in range(row):
            for j in range(col):
                if i == 0:
                    if not compare_col(j):
                        return False
                if j == 0:
                    if not compare_row(i):
                        return False
                if i % 3 == 0 and j % 3 == 0:
                    if not compare_square(i, j):
                        return False
        return True