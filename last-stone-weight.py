1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        for i in range(len(stones)):
4            stones[i] = -stones[i]
56        heapq.heapify(stones)
78        while len(stones) > 1:
9            largest = -heapq.heappop(stones)
10            second_largest = -heapq.heappop(stones)
11            diff = largest - second_largest
12            if diff != 0:
13                heapq.heappush(stones, -diff)
1415        if len(stones):
16            return -stones[0]
17        return 0
18