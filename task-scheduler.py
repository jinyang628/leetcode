import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        cooldown = deque([])
        track = Counter(tasks)
        for key, freq in track.items():
            heapq.heappush(heap, -freq)
        res = 0
        while heap or cooldown:
            res += 1
            if heap:
                curr = heapq.heappop(heap)
                curr += 1
                if curr < 0:
                    cooldown.append((curr, res + n))
            while cooldown and cooldown[0][1] <= res:
                freq, _ = cooldown.popleft()
                heapq.heappush(heap, freq)
        return res