from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        track = Counter(s)
        heap = []
        for item, freq in track.items():
            heapq.heappush(heap, (-freq, item))
        res = ""
        while heap:
            first_freq, first_item = heapq.heappop(heap)
            if res and first_item == res[-1]:
                if not heap:
                    return ""
                second_freq, second_item = heapq.heappop(heap)
                res += second_item
                res += first_item
                print(res)
                if second_freq + 1 != 0:
                    heapq.heappush(heap, (second_freq + 1, second_item))
                if first_freq + 1 != 0:
                    heapq.heappush(heap, (first_freq + 1, first_item))
            else:
                res += first_item
                if first_freq + 1 != 0:
                    heapq.heappush(heap, (first_freq + 1, first_item))
        return res