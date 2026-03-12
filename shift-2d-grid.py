1class Solution:
2    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        numbers = []
4        row, col = len(grid), len(grid[0])
5        for i in range(row):
6            for j in range(col):
7                numbers.append(grid[i][j])
8        numbers = deque(numbers)
9        for _ in range(k):
10            numbers.appendleft(numbers.pop())
11        res = [[0] * col for _ in range(row)]
12        count = 0
13        for i in range(row):
14            for j in range(col):
15                res[i][j] = numbers[count]
16                count += 1
17        return res