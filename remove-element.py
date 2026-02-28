1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        left = mid = 0
4        right = len(nums) - 1
5        res = 0
6        while mid <= right:
7            if nums[mid] != val:
8                nums[left], nums[mid] = nums[mid], nums[left]
9                left += 1
10                mid += 1
11                res += 1
12            else:
13                nums[mid], nums[right] = nums[right], nums[mid]
14                right -= 1
15        return res
16