1class Solution(object):
2    def isValidSudoku(self, board):
3        row, col = len(board), len(board[0])
45        def isValidSquare(r, c):
6            curr = board[r][c]
7            top_left_r = (r // 3) * 3
8            top_left_c = (c // 3) * 3
9            for i in range(top_left_r, top_left_r + 3):
10                for j in range(top_left_c, top_left_c + 3):
11                    if i == r and j == c:
12                        continue
13                    if board[i][j] == curr:
14                        return False
15            return True
1617        def isValidRow(r, c):
18            curr = board[r][c]
19            for i in range(col):
20                if i != c and board[r][i] == curr:
21                    return False
22            return True
2324        def isValidColumn(r, c):
25            curr = board[r][c]
26            for i in range(row):
27                if i != r and board[i][c] == curr:
28                    return False
29            return True
3031        for i in range(row):
32            for j in range(col):
33                if board[i][j] == ".":
34                    continue
35                if not (isValidSquare(i, j) and
36                        isValidRow(i, j) and
37                        isValidColumn(i, j)):
38                    return False
3940        return True
41