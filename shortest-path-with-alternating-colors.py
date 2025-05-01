import heapq
from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        distances = defaultdict(list) # key is node, value is a list containing shortest distance from red edge, and shortest distance from blue edge
        for i in range(n):
            distances[i] = [float('inf'), float('inf')]
        heap = [(0, 0, None)] # (distance, node, color)
        red_dict = defaultdict(list)
        blue_dict = defaultdict(list)
        for a, b in redEdges:
            red_dict[a].append(b)
        for a, b in blueEdges:
            blue_dict[a].append(b)
        while heap:
            distance, node, color = heapq.heappop(heap)
            if color is None:
                distances[node] = [0, 0]
                for neighbor in red_dict[node]:
                    heapq.heappush(heap, (distance + 1, neighbor, "red"))
                for neighbor in blue_dict[node]:
                    heapq.heappush(heap, (distance + 1, neighbor, "blue"))
            elif color == "blue":
                if distance > distances[node][1]:
                    continue 
                distances[node][1] = distance
                for neighbor in red_dict[node]:
                    heapq.heappush(heap, (distance + 1, neighbor, "red"))
            else:
                if distance > distances[node][0]:
                    continue
                distances[node][0] = distance
                for neighbor in blue_dict[node]:
                    heapq.heappush(heap, (distance + 1, neighbor, "blue")) 
        res = [-1] * n
        for i in range(n):
            if distances[i][0] == float('inf') and distances[i][1] == float('inf'):
                res[i] = -1
            else:
                res[i] = min(distances[i])
        return res