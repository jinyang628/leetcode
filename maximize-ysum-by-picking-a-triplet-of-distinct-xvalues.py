1class Solution:
2    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
3        idx_tracker = defaultdict(list)
4        for idx, num in enumerate(x):
5            idx_tracker[num].append(idx)
67        candidates = []
8        for _, indexes in idx_tracker.items():
9            maxSoFar = 0
10            for idx in indexes:
11                maxSoFar = max(maxSoFar, y[idx])
12            candidates.append(-maxSoFar)
1314        heapq.heapify(candidates)
15        res = 0
16        if len(candidates) < 3:
17            return -1
18        for _ in range(3):
19            res += -heapq.heappop(candidates)
20        return res
21