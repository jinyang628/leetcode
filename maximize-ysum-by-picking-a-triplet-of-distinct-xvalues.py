1class Solution:
2    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
3        groupings = defaultdict(list)
4        for idx, num in enumerate(x):
5            groupings[num].append(y[idx])
6        largest_in_group = []
7        for _, items in groupings.items():
8            largest_in_group.append(-max(items))
9        if len(largest_in_group) <= 2:
10            return -1
11        heapq.heapify(largest_in_group)
12        res = 0
13        for _ in range(3):
14            res += -heapq.heappop(largest_in_group)
15        return res