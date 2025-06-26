class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        row_locations = defaultdict(list)
        col_locations = defaultdict(list)
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    row_locations[i].append(j)
                    col_locations[j].append(i)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] and (len(row_locations[i]) > 1 or len(col_locations[j]) > 1):
                    count += 1
        return count