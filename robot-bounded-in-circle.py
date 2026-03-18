1class Solution:
2    def isRobotBounded(self, instructions: str) -> bool:
3        direction = (0, -1) # x, y
4        curr = (0, 0)
5        for instruction in instructions:
6            if instruction == "G":
7                curr = tuple(a + b for a, b in zip(curr, direction))
8            elif instruction == "L":
9                if direction == (0, -1):
10                    direction = (-1, 0)
11                elif direction == (-1, 0):
12                    direction = (0, 1)
13                elif direction == (0, 1):
14                    direction = (1, 0)
15                else:
16                    direction = (0, -1)
17            elif instruction == "R":
18                if direction == (0, -1):
19                    direction = (1, 0)
20                elif direction == (1, 0):
21                    direction = (0, 1)
22                elif direction == (0, 1):
23                    direction = (-1, 0)
24                else:
25                    direction = (0, -1)
26        if curr == (0, 0):
27            return True
28        if direction != (0, -1):
29            return True
30        return False