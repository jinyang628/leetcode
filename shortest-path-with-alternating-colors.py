1from collections import deque
23class Solution:
4    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
5        res = [float('inf')] * n
6        red_neighbors = defaultdict(list)
7        blue_neighbors = defaultdict(list)
8        for a, b in redEdges:
9            red_neighbors[a].append(b)
10        for a, b in blueEdges:
11            blue_neighbors[a].append(b)
1213        red_visited = set()
14        red_queue = deque([(0, 0, True)])
15        while red_queue:
16            node, dist, is_red = red_queue.popleft()
17            if (node, is_red) in red_visited:
18                continue
19            red_visited.add((node, is_red))
20            res[node] = min(res[node], dist)
21            if is_red:
22                for neighbor in blue_neighbors[node]:
23                    red_queue.append((neighbor, dist + 1, not is_red))
24            else:
25                for neighbor in red_neighbors[node]:
26                    red_queue.append((neighbor, dist + 1, not is_red))
27        blue_visited = set()
28        blue_queue = deque([(0, 0, False)])
29        while blue_queue:
30            node, dist, is_red = blue_queue.popleft()
31            if (node, is_red) in blue_visited:
32                continue
33            blue_visited.add((node, is_red))
34            res[node] = min(res[node], dist)
35            if is_red:
36                for neighbor in blue_neighbors[node]:
37                    blue_queue.append((neighbor, dist + 1, not is_red))
38            else:
39                for neighbor in red_neighbors[node]:
40                    blue_queue.append((neighbor, dist + 1, not is_red))
4142        for idx, num in enumerate(res):
43            if num == float('inf'):
44                res[idx] = -1
45        return res