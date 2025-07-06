class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestSoFar = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            original = arr[i]
            arr[i] = greatestSoFar
            greatestSoFar = max(greatestSoFar, original)
        return arr