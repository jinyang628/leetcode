class Solution(object):
    def minimumEffortPath(self, heights):
        """
        """
        m = len(heights)
        n = len(heights[0])
        q = []
        heapq.heappush(q, (0,0,0))
        visited = [[False for i in range(n)] for j in range(m)]
        while q:
            curr = heapq.heappop(q)
            if visited[curr[1]][curr[2]]:
                continue
            if curr[1] == m - 1 and curr[2] == n - 1:
                return curr[0]
            visited[curr[1]][curr[2]] = True
            for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = curr[1] + _x, curr[2] + _y
                if 0 <= x < m and 0 <= y < n:
                    heapq.heappush(q, (max(curr[0], abs(heights[x][y] - heights[curr[1]][curr[2]])), x, y))