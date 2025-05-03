from collections import defaultdict
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        neighbors = defaultdict(list)
        for a, b, time in edges:
            neighbors[a].append((b, time))
            neighbors[b].append((a, time))
        maxSoFar = [0]
        def dfs(node: int, timeSoFar: int, valueSoFar: int, visited: set) -> None:
            if timeSoFar > maxTime:
                return
            if node == 0:
                maxSoFar[0] = max(maxSoFar[0], valueSoFar)
            for neighbor, time in neighbors[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    dfs(neighbor, timeSoFar + time, valueSoFar + values[neighbor], visited)
                    visited.pop()
                else:
                    dfs(neighbor, timeSoFar + time, valueSoFar, visited)
        dfs(0, 0, values[0], [0])
        return maxSoFar[0]