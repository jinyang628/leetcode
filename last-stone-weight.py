import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if first == second:
                continue
            heapq.heappush(stones, -abs(second - first))
        return abs(stones[0]) if stones else 0