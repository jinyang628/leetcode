import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diffs = []
        for i in range(1, len(heights)):
            if heights[i] <= heights[i - 1]:
                diffs.append(0)
            else:
                diffs.append(heights[i] - heights[i - 1])
        heap = []
        i = -1
        for i in range(len(diffs)):
            if not diffs[i]:
                continue 
            heapq.heappush(heap, diffs[i])
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return i + 1