import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def get_distance(x: int, y: int) -> int:
            return math.sqrt(x**2 + y**2)
        for x, y in points:
            dist = get_distance(x, y)
            heapq.heappush(heap, (dist, [x, y]))
        res = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            res.append(point)
        return res