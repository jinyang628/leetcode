1class Solution:
2    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
3        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
4        row, col = len(board), len(board[0])
5        for dr, dc in directions:
6            path_length = 1
7            is_exit = False
8            new_r, new_c = rMove, cMove
9            while not is_exit:
10                new_r += dr
11                new_c += dc
12                if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
13                    is_exit = True
14                    continue
15                print(new_r, new_c)
16                path_length += 1
17                if board[new_r][new_c] == color:
18                    if path_length < 3:
19                        is_exit = True
20                    else:
21                        return True
22                elif board[new_r][new_c] == ".":
23                    is_exit = True
2425        return False
26