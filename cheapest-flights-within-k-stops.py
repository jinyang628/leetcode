import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        track = defaultdict(list)
        for f, t, p in flights:
            track[f].append((p, t))
        heap = [(0, 0, src)] # costSoFar, stops, node
        visited = {} # key is node and value is stops
        while heap:
            costSoFar, stops, node = heapq.heappop(heap)
            if node == dst:
                return costSoFar
            if stops > k:
                continue
            if node in visited and visited[node] <= stops:
                continue
            visited[node] = stops
            for price, target in track[node]:
                heapq.heappush(heap, (costSoFar + price, stops + 1,  target))
        return -1