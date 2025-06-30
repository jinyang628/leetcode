class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            curr = -heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(curr)))
        return -sum(gifts)