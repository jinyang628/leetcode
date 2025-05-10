class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x = y = 0
        for command in commands:
            if command == "UP":
                y -= 1
            elif command == "RIGHT":
                x += 1
            elif command == "LEFT":
                x -= 1
            else:
                y += 1
        return y * n + x