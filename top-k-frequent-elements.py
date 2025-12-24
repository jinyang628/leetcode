1from collections import Counter
2import heapq
3class Solution(object):
4    def topKFrequent(self, nums, k):
5        """
6789        """
10        count = Counter(nums)
11        heap = []
12        for key, value in count.items():
13            heap.append((-value, key))
14        heapq.heapify(heap)
15        res = []
16        for _ in range(k):
17            _, num = heapq.heappop(heap)
18            res.append(num)
19        return res