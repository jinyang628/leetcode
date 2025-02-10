from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = Counter(nums)
        heap = []
        for key, freq in track.items():
            heapq.heappush(heap, (-freq, key))
        res = []
        for _ in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        return res