from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        track = defaultdict(list)
        for a, b in edges:
            track[a].append(b)
            track[b].append(a)
        queue = deque([i for i in range(n) if len(track[i]) == 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                neighbors = track[curr]
                for neighbor in neighbors:
                    track[neighbor].remove(curr)
                    if len(track[neighbor]) == 1:
                        queue.append(neighbor)
        return list(queue)