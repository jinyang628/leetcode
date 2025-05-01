from collections import defaultdict, deque
class Solution:
    def get_graph(self, node: int, edges: dict) -> dict:
        graph = {}
        queue = deque([(0, node)])
        visited = set()
        while queue:
            dist, node = queue.popleft()
            if node in visited:
                continue
            graph[node] = dist
            visited.add(node)
            for neighbor in edges[node]:
                queue.append((dist + 1, neighbor))
        return graph
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:    
        track = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] == -1:
                continue
            track[i].append(edges[i])
        one_graph = self.get_graph(node1, track)
        two_graph = self.get_graph(node2, track)
        minSoFar = (-1, float('inf')) # candidate node, min of max distance
        for i in range(len(edges)):
            if i not in one_graph or i not in two_graph:
                continue
            one_dist = one_graph[i]
            two_dist = two_graph[i]
            max_dist = max(one_dist, two_dist)
            if max_dist < minSoFar[1]:
                minSoFar = (i, max_dist)
        return minSoFar[0]