1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        def getDist(first: list[int], second: list[int]) -> int:
4            return abs(second[0] - first[0]) + abs(second[1] - first[1])
5        tracker = defaultdict(list)
6        for i in range(len(points) - 1):
7            for j in range(i + 1, len(points)):
8                dist = getDist(points[i], points[j])
9                tracker[i].append(
10                    (dist,j)
11                )
12                tracker[j].append(
13                    (dist,i)
14                )
15        visited = set()
16        heap = [(0, 0)]
17        total_dist = 0
18        while len(visited) != len(points):
19            dist, point_idx = heapq.heappop(heap)
20            if point_idx in visited:
21                continue
22            visited.add(point_idx)
23            total_dist += dist
24            for new_dist, new_point_idx in tracker[point_idx]:
25                if new_point_idx in visited:
26                    continue
27                heapq.heappush(heap, (new_dist, new_point_idx))
2829        return total_dist
303132