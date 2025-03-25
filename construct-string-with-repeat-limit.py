from collections import Counter, defaultdict
import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        track = Counter(s)
        timer = defaultdict(int)
        heap = []
        for key, freq in track.items():
            heapq.heappush(heap, (-ord(key), freq))
        res = []
        cooldown = None
        while heap:
            negative_ord, freq = heapq.heappop(heap)
            res.append(chr(-negative_ord))
            timer[negative_ord] += 1
            if cooldown:
                timer[negative_ord] = 0
                heapq.heappush(heap, cooldown)
                cooldown = None
            freq -= 1
            if freq > 0:
                if timer[negative_ord] == repeatLimit:
                    timer[negative_ord] = 0
                    cooldown = (negative_ord, freq)
                else:
                    heapq.heappush(heap, (negative_ord, freq))
        return "".join(res)