1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4        while left <= right:
5            mid = left + (right - left) // 2
6            if nums[mid] == target:
7                return mid
8            elif nums[mid] < target:
9                left = mid + 1
10            else:
11                right = mid - 1
12        return left