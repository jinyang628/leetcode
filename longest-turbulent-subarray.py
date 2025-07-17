class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSoFar = right = 1
        left = 0
        isRising = None
        while right < len(arr):
            print(left, right, isRising, maxSoFar)
            if arr[right] > arr[right - 1] and (isRising or isRising is None):
                isRising = False
            elif arr[right] < arr[right - 1] and (not isRising):
                isRising = True
            else:
                maxSoFar = max(maxSoFar, (right - left))
                if arr[right] == arr[right - 1]:
                    left = right
                else:
                    left = right - 1
            right += 1
        return max(maxSoFar, right - left)