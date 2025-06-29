import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        neighbors = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            neighbors[a].append((b, prob))
            neighbors[b].append((a, prob))
        heap = [(-1, start_node, None)]
        while heap:
            negative_prob, node, parent = heapq.heappop(heap)
            prob = -negative_prob
            if node == end_node:
                return prob
            for neighbor, probability in neighbors[node]:
                if neighbor == parent:
                    continue
                heapq.heappush(heap, (-(probability * prob), neighbor, node))
        return 0