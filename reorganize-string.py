from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        track = Counter(s)
        cooldown = None
        heap = []
        for key, freq in track.items():
            heapq.heappush(heap, (-freq, key))
        time = 0
        res = ""
        while heap:
            _, key = heapq.heappop(heap)
            track[key] -= 1
            res += key
            if cooldown is not None and track[cooldown]:
                heapq.heappush(heap, (-track[cooldown], cooldown))
            cooldown = key
            time += 1
        return res if not track[cooldown] else ""