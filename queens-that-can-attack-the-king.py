class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = set()
        for x, y in queens:
            queen_set.add((x, y))
        # start from king's perspective, break when see the first queen in that direction
        res = []
        def peek(x: int, y: int, delta_x: int, delta_y: int) -> None:
            if x < 0 or y < 0 or x >= 8 or y >= 8:
                return 
            if (x, y) in queen_set:
                res.append([x, y])
                return 
            peek(x + delta_x, y + delta_y, delta_x, delta_y)
        kx, ky = king[0], king[1]
        # top left
        peek(kx, ky, -1, -1)
        # top
        peek(kx, ky, 0, -1)
        # top right
        peek(kx, ky, 1, -1)
        # right
        peek(kx, ky, 1, 0)
        # bot right
        peek(kx, ky, 1, 1)
        # bot
        peek(kx, ky, 0, 1)
        # bot left
        peek(kx, ky, -1, 1)
        # left
        peek(kx, ky, -1, 0)
        return res