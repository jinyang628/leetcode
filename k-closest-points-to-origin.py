import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dists.append((x**2 + y**2, x, y))
        heapq.heapify(dists)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(dists)
            res.append([x,y])
        return res