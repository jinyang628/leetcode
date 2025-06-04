class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSoFar = 0
        for i in range(len(arr) - 1, -1, -1):
            tmp = maxSoFar
            maxSoFar = max(arr[i], maxSoFar)
            arr[i] = tmp
        arr[-1] = -1
        return arr