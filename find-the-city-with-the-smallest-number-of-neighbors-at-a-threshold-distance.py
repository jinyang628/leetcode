from collections import defaultdict
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        neighbors = defaultdict(list)
        for a, b, dist in edges:
            neighbors[a].append((dist, b))
            neighbors[b].append((dist, a))
        maxSoFar = (n, float('inf')) # key is node, vlaue is the number of cities it is connected to
        for i in range(n - 1, -1, -1):
            heap = [(0, i)] # key is distance, value is node
            visited = set()
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visited:
                    continue 
                if dist > distanceThreshold:
                    continue
                visited.add(node)
                for d, n in neighbors[node]:
                    heapq.heappush(heap, (d + dist, n))
            if maxSoFar[1] > len(visited):
                maxSoFar = (i, len(visited))
        return maxSoFar[0]