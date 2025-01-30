from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        track = Counter(s)
        heap = []
        for key, freq in track.items():
            heapq.heappush(heap, (-freq, key))
        res = ""
        while heap:
            first_negative_freq, first_key = heapq.heappop(heap)
            if res and res[-1] == first_key:
                if not heap:
                    return ""
                second_negative_freq, second_key = heapq.heappop(heap)
                second_negative_freq += 1
                res += second_key
                if second_negative_freq != 0:
                    heapq.heappush(heap, (second_negative_freq, second_key))
                heapq.heappush(heap, (first_negative_freq, first_key))
            else:
                res += first_key
                first_negative_freq += 1
                if first_negative_freq == 0:
                    continue
                heapq.heappush(heap, (first_negative_freq, first_key))
        return res