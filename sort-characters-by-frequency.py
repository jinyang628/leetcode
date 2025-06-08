from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for key, freq in count.items():
            heapq.heappush(heap, (-freq, key))
        res = []
        while heap:
            negative_freq, key = heapq.heappop(heap)
            res.extend([key] * -negative_freq)
        return "".join(res)