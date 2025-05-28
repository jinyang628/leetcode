class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        length = len(arrays)
        minSoFar, maxSoFar = arrays[0][0], arrays[0][-1]
        res = 0
        for array in arrays[1:]:
            res = max(
                res, abs(maxSoFar - array[0]), abs(array[-1] - minSoFar) 
            )
            maxSoFar = max(maxSoFar, array[-1])
            minSoFar = min(minSoFar, array[0])
        return res