from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        track = defaultdict(list)
        for source, target, time in times:
            track[source].append((target, time))
        visited = set()
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue 
            visited.add(node)
            if len(visited) == n:
                return time
            for target, distance in track[node]:
                heapq.heappush(heap, (time + distance, target))
        return -1