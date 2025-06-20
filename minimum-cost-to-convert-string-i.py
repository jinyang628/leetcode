import heapq
from collections import defaultdict
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target):
            return -1
        track = defaultdict(list)
        dist_map = defaultdict(dict)
        for o, c, w in zip(original, changed, cost):
            track[o].append((c, w))
        res = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            if target[i] in dist_map[source[i]]:
                res += dist_map[source[i]][target[i]]
                continue
            total = None
            heap = [(0, source[i])]
            distances = {}
            while heap:
                dist, curr = heapq.heappop(heap)
                if curr == target[i]:
                    total = dist
                    res += dist
                    break
                if curr in distances:
                    continue
                distances[curr] = dist
                for neighbor, price in track[curr]:
                    if neighbor in distances:
                        continue
                    heapq.heappush(heap, (dist + price, neighbor))
            if total is None:
                return -1
            dist_map[source[i]] = distances
        return res