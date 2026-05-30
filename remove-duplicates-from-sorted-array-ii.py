1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        left = right = 0
4        while right < len(nums):
5            if left < 2 or nums[right] != nums[left - 2]:
6                nums[left], nums[right] = nums[right], nums[left]
7                left += 1
8                right += 1
9            else:
10                right += 1
11        return left
12