import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def check(idx: int) -> bool:
            if idx < 1:
                return True 
            subset = heights[:idx + 1]
            diffs = []
            for i in range(1, idx + 1):
                diff = subset[i] - subset[i - 1]
                if diff > 0:
                    diffs.append(-diff)
            heapq.heapify(diffs)
            for _ in range(ladders):
                if not diffs:
                    break
                heapq.heappop(diffs)
            bricks_needed = -sum(diffs)
            return bricks_needed <= bricks
        left, right = 0, len(heights) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right