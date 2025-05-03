class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0] * len(graph)
        def dfs(node: int) -> bool:
            if colors[node] != 0:
                return colors[node] == 2
            colors[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            colors[node] = 2
            return True
        return [i for i in range(len(graph)) if dfs(i)]