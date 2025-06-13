import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for val, qty in count.items():
            heap.append((-qty, val))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]