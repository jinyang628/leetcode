class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, ranks[0] * cars ** 2
        def isPossible(time: int) -> bool:
            numCars = 0
            for rank in ranks:
                numCars += math.floor(math.sqrt(time / rank))
                if numCars >= cars:
                    return True
            return False
        while left <= right:
            mid = left + (right - left) // 2
            if isPossible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left