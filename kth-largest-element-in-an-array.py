1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heap = []
4        for num in nums:
5            heap.append(-num)
6        heapq.heapify(heap)
7        for _ in range(k):
8            num = -heapq.heappop(heap)
91011        return num