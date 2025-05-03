import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        time = 0
        row, col = len(moveTime), len(moveTime[0])
        def time_taken(x: int, y: int, currTime: int) -> int:
            if x < 0 or y < 0 or x >= row or y >= col:
                return float('inf')
            openingTime = moveTime[x][y]
            if currTime >= openingTime:
                return currTime + 1
            else:
                return openingTime + 1
        heap = [(0, 0, 0)] # time, x, y
        visited = set()
        while heap:
            time, x, y = heapq.heappop(heap)
            if (x, y) == (row - 1, col - 1):
                return time 
            if (x, y) in visited:
                continue
            visited.add((x, y))
            times = {
                (x - 1, y): time_taken(x - 1, y, time),
                (x + 1, y): time_taken(x + 1, y, time),
                (x, y - 1): time_taken(x, y - 1, time),
                (x, y + 1): time_taken(x, y + 1, time)
            }
            for coord, time in times.items():
                if time == float('inf'):
                    continue
                heapq.heappush(heap, (time, coord[0], coord[1]))