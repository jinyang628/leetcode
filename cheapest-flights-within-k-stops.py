from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        track = defaultdict(list)
        distances = {}
        for i in range(n):
            distances[i] = float('inf')
        for s, d, dist in flights:
            track[s].append((d, dist))
        heap = [(0, 0, src)]
        while heap:
            steps, dist, node = heapq.heappop(heap)
            if steps > k + 1:
                break
            print(steps, dist, node, distances)
            if distances[node] > dist:
                distances[node] = dist
                for neighbor, weight in track[node]:
                    heapq.heappush(heap, (steps + 1, weight + dist, neighbor))
        return distances[dst] if distances[dst] != float('inf') else -1