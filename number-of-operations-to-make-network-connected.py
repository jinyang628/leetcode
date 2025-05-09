from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = defaultdict(list)
        for a, b in connections:
            edges[a].append(b)
            edges[b].append(a)
        num_cables = len(connections)
        if num_cables < (n - 1):
            return -1
        components: int = 0
        visited = set()
        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            for neighbor in edges[node]:
                dfs(neighbor)
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components - 1