import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)
        for _ in range(k):
            curr = heapq.heappop(gifts)
            curr /= -math.sqrt(-curr)
            heapq.heappush(gifts, -math.floor(curr))
        return -sum(gifts)