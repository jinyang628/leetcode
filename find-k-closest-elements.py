1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        heap = []
4        for idx, num in enumerate(arr):
5            heap.append((abs(num - x), num))
6        heapq.heapify(heap)
7        res = []
8        for _ in range(k):
9            _, num = heapq.heappop(heap)
10            res.append(num)
11        res.sort()
12        return res