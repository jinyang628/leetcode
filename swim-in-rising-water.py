from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        minHeightNow = 0
        stack = []
        tooHighLand = defaultdict(list) # key is height, value is a list of the lands that that require that minimum height
        stack.append((0,0))
        while True:
            if stack:
                r, c = stack.pop()
                if r < 0 or r >= row or c < 0 or c >= col:
                    continue
                if visited[r][c]:
                    continue 
                if grid[r][c] > minHeightNow:
                    tooHighLand[grid[r][c]].append((r, c))
                    continue 
                if r == row - 1 and c == col - 1:
                    return minHeightNow
                visited[r][c] = True
                stack.append((r-1, c))
                stack.append((r+1, c))
                stack.append((r, c-1))
                stack.append((r, c+1))
            else:
                minHeightNow = min(tooHighLand.keys())
                for unlockedLand in tooHighLand[minHeightNow]:
                    stack.append(unlockedLand)
                del tooHighLand[minHeightNow]
        return minHeightNow