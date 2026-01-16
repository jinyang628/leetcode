1from collections import defaultdict
2import heapq
3class Solution:
4    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
5        track = defaultdict(list)
6        for u, v, w in times:
7            track[u].append((v, w))
8        visited = set()
9        heap = [(0, k)]
10        while heap:
11            time, node = heapq.heappop(heap)
12            if node in visited:
13                continue
14            visited.add(node)
15            if len(visited) == n:
16                return time
17            for neighbor, dist in track[node]:
18                if neighbor in visited:
19                    continue
20                heapq.heappush(heap, (dist + time, neighbor))
21        if len(visited) == n:
22            return time
23        return -1
2425