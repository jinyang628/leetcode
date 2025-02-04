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
            count = 0
            res += 1
            for freq, time in cooldown:
                if time > res:
                    break
                count += 1
                heapq.heappush(heap, freq)
            for _ in range(count):
                cooldown.popleft()
            if not heap:
                continue
            curr = heapq.heappop(heap)
            curr += 1
            if curr < 0:
                cooldown.append((curr, res + n + 1))
        return res