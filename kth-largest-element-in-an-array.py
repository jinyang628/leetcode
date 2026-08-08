1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        for idx, num in enumerate(nums):
4            nums[idx] = -num
5        heapq.heapify(nums)
6        for _ in range(k):
7            res = -heapq.heappop(nums)
8        return res