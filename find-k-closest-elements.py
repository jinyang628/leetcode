class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)
        while right - left > k:
            left_diff = abs(x - arr[left])
            right_diff = abs(x - arr[right - 1])
            if left_diff <= right_diff:
                right -= 1
            else:
                left += 1
        return arr[left: right]