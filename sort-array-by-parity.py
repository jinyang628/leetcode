1class Solution:
2    def sortArrayByParity(self, nums: List[int]) -> List[int]:
3        left = right = 0
4        while right < len(nums):
5            if nums[right] % 2 == 0:
6                nums[left], nums[right] = nums[right], nums[left]
7                left += 1
8                right += 1
9            else:
10                right += 1
11        return nums