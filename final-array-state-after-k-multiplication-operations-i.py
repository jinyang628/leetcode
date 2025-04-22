import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        for _ in range(k):
            num, idx = heapq.heappop(heap)
            num *= multiplier
            heapq.heappush(heap, (num, idx))
        res = [0] * len(nums)
        while heap:
            num, idx = heapq.heappop(heap)
            res[idx] = num
        return res