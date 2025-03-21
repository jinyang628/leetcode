class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        """
        row, col = len(board), len(board[0])
        res = [[0] * col for _ in range(row)]
        def checkValue(r: int, c: int) -> Optional[int]:
            if r < 0 or r >= row or c < 0 or c >= col:
                return None
            return board[r][c] 
        def checkLife(r: int, c: int) -> int:
            curr = board[r][c]
            count = 0
            count += 1 if checkValue(r - 1, c - 1) == 1 else 0
            count += 1 if checkValue(r - 1, c) == 1 else 0
            count += 1 if checkValue(r - 1, c + 1) == 1 else 0
            count += 1 if checkValue(r + 1, c - 1) == 1 else 0
            count += 1 if checkValue(r + 1, c) == 1 else 0
            count += 1 if checkValue(r + 1, c + 1) == 1 else 0
            count += 1 if checkValue(r, c - 1) == 1 else 0
            count += 1 if checkValue(r, c + 1) == 1 else 0
            if curr == 0:
                return 1 if count == 3 else 0
            else:
                if count < 2:
                    return 0
                elif count <= 3:
                    return 1
                else:
                    return 0
        for i in range(row):
            for j in range(col):
                res[i][j] = checkLife(i, j)
        for i in range(row):
            for j in range(col):
                board[i][j] = res[i][j]